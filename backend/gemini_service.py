import google.generativeai as genai
import os
import logging
from typing import Optional

logger = logging.getLogger(__name__)


class GeminiService:
    """Serviço para integração com a API do Gemini"""
    
    def __init__(self):
        self.api_key = os.getenv("GOOGLE_API_KEY")
        self.model_name = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")
        
        if not self.api_key:
            logger.error("GOOGLE_API_KEY não configurada no .env")
            raise ValueError("GOOGLE_API_KEY não configurada")
        
        genai.configure(api_key=self.api_key)
        logger.info(f"Gemini configurado com modelo: {self.model_name}")
    
    def gerar_conteudo(self, prompt: str) -> Optional[str]:
        """
        Gera conteúdo usando o modelo Gemini.
        
        Args:
            prompt: O prompt a ser enviado para o modelo
            
        Returns:
            O texto gerado ou None em caso de erro
        """
        try:
            model = genai.GenerativeModel(self.model_name)
            response = model.generate_content(prompt)
            
            if response and response.text:
                logger.info("Conteúdo gerado com sucesso")
                return response.text
            else:
                logger.warning("Resposta vazia do Gemini")
                return None
                
        except Exception as e:
            logger.error(f"Erro ao chamar Gemini: {str(e)}")
            raise
