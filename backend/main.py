from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ValidationError
import logging
import os
from dotenv import load_dotenv

from models import EstudoRequest, EstudoResponse, ErrorResponse, OpcoesResponse
from prompts import gerar_prompt
from gemini_service import GeminiService

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Carrega variáveis do .env
load_dotenv()

# Inicializa o app FastAPI
app = FastAPI(
    title="StudyIA API",
    description="API de assistente de estudos integrada com Gemini",
    version="1.0.0"
)

# Configura CORS para permitir requisições do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especifique as origens permitidas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Tenta inicializar o serviço Gemini (pode falhar se a chave não estiver configurada)
try:
    gemini_service = GeminiService()
    logger.info("Serviço Gemini inicializado com sucesso")
except ValueError as e:
    gemini_service = None
    logger.warning(f"Serviço Gemini não inicializado: {e}")


# Lista de palavras/assuntos bloqueados (conteúdo ofensivo ou perigoso)
ASSUNTOS_BLOQUEADOS = [
    "como fazer bomba",
    "como fabricar droga",
    "como hackear",
    "como invadir",
    "como piratear",
    "como matar",
    "como suicidar",
    "como roubar",
    "como fraude",
    "como golpear"
]


def validar_assunto_permitido(assunto: str) -> bool:
    """
    Verifica se o assunto não contém termos bloqueados.
    """
    assunto_lower = assunto.lower()
    for bloqueado in ASSUNTOS_BLOQUEADOS:
        if bloqueado in assunto_lower:
            return False
    return True


@app.get("/", tags=["Health"])
def root():
    """Endpoint raiz - verifica se a API está funcionando"""
    return {"mensagem": "StudyIA API funcionando"}


@app.get("/health", tags=["Health"])
def health():
    """Endpoint de health check"""
    return {"status": "ok"}


@app.get("/opcoes", response_model=OpcoesResponse, tags=["Configuração"])
def opcoes():
    """Retorna os níveis e tipos permitidos"""
    return {
        "niveis": ["iniciante", "intermediario", "avancado"],
        "tipos": ["explicacao", "resumo", "quiz", "perguntas"]
    }


@app.post("/estudo", response_model=EstudoResponse, tags=["Estudo"])
def criar_estudo(request: EstudoRequest):
    """
    Endpoint principal - gera conteúdo de estudo usando o Gemini.
    
    Recebe matéria, assunto, nível e tipo, e retorna o conteúdo gerado.
    """
    # Validação de negócio: verificar se o assunto é permitido
    if not validar_assunto_permitido(request.assunto):
        logger.warning(f"Assunto bloqueado: {request.assunto}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"erro": "Este assunto não é permitido para fins de estudo."}
        )
    
    # Verifica se o serviço Gemini está configurado
    if gemini_service is None:
        logger.error("Tentativa de uso sem chave do Gemini configurada")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"erro": "Serviço de IA não configurado."}
        )
    
    # Gera o prompt apropriado
    prompt = gerar_prompt(
        materia=request.materia,
        assunto=request.assunto,
        nivel=request.nivel,
        tipo=request.tipo
    )
    
    logger.info(f"Gerando conteúdo: {request.materia} - {request.assunto} - {request.tipo}")
    
    try:
        # Chama o Gemini
        resposta_texto = gemini_service.gerar_conteudo(prompt)
        
        if not resposta_texto:
            logger.error("Resposta vazia do Gemini")
            raise HTTPException(
                status_code=status.HTTP_502_BAD_GATEWAY,
                detail={"erro": "Não foi possível gerar o conteúdo no momento."}
            )
        
        # Retorna a resposta
        return EstudoResponse(
            materia=request.materia,
            assunto=request.assunto,
            nivel=request.nivel,
            tipo=request.tipo,
            resposta=resposta_texto
        )
        
    except HTTPException:
        # Re-levanta exceções HTTP já tratadas
        raise
        
    except Exception as e:
        # Captura erros da chamada ao Gemini
        error_str = str(e).lower()
        
        # Verifica se é erro de limite de uso (429)
        if "429" in error_str or "quota" in error_str or "limit" in error_str:
            logger.warning(f"Limite de uso do Gemini atingido: {e}")
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail={"erro": "Muitas requisições. Tente novamente em instantes."}
            )
        
        # Outros erros (timeout, serviço fora do ar, etc)
        logger.error(f"Erro ao gerar conteúdo: {e}")
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail={"erro": "Não foi possível gerar o conteúdo no momento."}
        )


# Tratamento global de erros de validação do Pydantic
@app.exception_handler(ValidationError)
def validation_exception_handler(request, exc):
    """Converte erros de validação do Pydantic para respostas amigáveis"""
    errors = exc.errors()
    messages = []
    
    for error in errors:
        field = error["loc"][-1] if error["loc"] else "campo"
        msg = error["msg"]
        
        # Mensagens personalizadas para campos específicos
        if field == "materia":
            messages.append("A matéria é obrigatória e deve ter entre 2 e 80 caracteres.")
        elif field == "assunto":
            messages.append("O assunto é obrigatório e deve ter entre 3 e 150 caracteres.")
        elif field in ["nivel", "tipo"]:
            messages.append(f"Valor inválido para {field}.")
        else:
            messages.append(f"{field}: {msg}")
    
    return ErrorResponse(erro="; ".join(messages))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
