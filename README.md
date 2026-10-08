# 📚 StudyIA - Assistente de Estudos com Gemini

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green.svg)
![React Native](https://img.shields.io/badge/React_Native-Expo-blue.svg)
![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)
![Status](https://img.shields.io/badge/Status-Completo-success.svg)

---

## 📖 Descrição do Produto

O **StudyIA** é um assistente de estudos inteligente que utiliza a API do Google Gemini para gerar conteúdo educacional personalizado. 

### Problema que Resolve
Estudantes frequentemente enfrentam dificuldades em encontrar material de estudo adequado ao seu nível de conhecimento. O conteúdo disponível na internet é genérico e não se adapta às necessidades individuais de aprendizado.

### Solução Proposta
O StudyIA permite que o usuário informe a matéria, o assunto, seu nível de conhecimento e o tipo de conteúdo desejado. O sistema gera automaticamente:
- **Explicações** didáticas com exemplos práticos
- **Resumos** em tópicos dos pontos principais
- **Quizzes** com questões de múltipla escolha e gabarito
- **Perguntas** de estudo para revisão

### Público-Alvo
- Estudantes de ensino médio e superior
- Profissionais em busca de reciclagem
- Entusiastas que desejam aprender novos assuntos

---

## 🏗️ Arquitetura do Sistema

```
┌─────────────────────────────────────────────────────────────┐
│                    React Native (Expo)                     │
│                   Frontend Web (Interface)                  │
│              http://localhost:19006                         │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  • Tela de Formulário                                │  │
│  │  • Tela de Resultado                                 │  │
│  │  • Validação Frontend                                │  │
│  └──────────────────────────────────────────────────────┘  │
└──────────────────────────┬──────────────────────────────────┘
                           │ HTTP/JSON
                           │
┌──────────────────────────▼──────────────────────────────────┐
│                      FastAPI (Python)                       │
│              http://127.0.0.1:8000                          │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  • Validação de Dados (Pydantic)                    │  │
│  │  • Regras de Negócio                                 │  │
│  │  • Geração de Prompts                                │  │
│  │  • Tratamento de Erros                               │  │
│  └──────────────────────────────────────────────────────┘  │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           │
┌──────────────────────────▼──────────────────────────────────┐
│                   GeminiService (Backend)                    │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  • Configuração da API Key                          │  │
│  │  • Chamada ao Modelo Gemini                         │  │
│  │  • Tratamento de Respostas                           │  │
│  └──────────────────────────────────────────────────────┘  │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           │
┌──────────────────────────▼──────────────────────────────────┐
│                    Google Gemini API                         │
│              Modelo: gemini-3.8-flash                        │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  • Processamento de Linguagem Natural               │  │
│  │  • Geração de Conteúdo Educacional                   │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Fluxo de Dados
```
Usuário → Frontend → API FastAPI → Validação → Prompt → Gemini → Resposta → Frontend → Usuário
```

---

## 🛠️ Tecnologias Utilizadas

### Backend
- **Python 3.10+** - Linguagem de programação
- **FastAPI** - Framework web moderno e performático
- **Uvicorn** - Servidor ASGI para executar o FastAPI
- **Pydantic** - Validação de dados e definição de schemas
- **python-dotenv** - Gerenciamento de variáveis de ambiente
- **google-generativeai** - Biblioteca oficial do Google Gemini

### Frontend
- **React Native** - Framework para desenvolvimento mobile/web
- **Expo** - Ferramenta para desenvolvimento React Native
- **React Native Web** - Rodar React Native no navegador

---

## 🚀 Como Executar do Zero

### Pré-requisitos
- **Python 3.10 ou superior** - [Download](https://www.python.org/downloads/)
- **Node.js 18+** - [Download](https://nodejs.org/)
- **Chave da API do Gemini** - Obtenha em [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

---

### Passo 1: Clonar o Projeto

```bash
git clone <url-do-repositorio>
cd studyia
```

---

### Passo 2: Configurar o Backend

**1. Navegue até a pasta do backend:**
```powershell
cd caminho/para/studyia/backend
```

**2. Crie o ambiente virtual:**
```powershell
python -m venv venv
```

**3. Ative o ambiente virtual:**
```powershell
.\venv\Scripts\activate
```

**4. Instale as dependências:**
```powershell
pip install -r requirements.txt
```

**5. Crie o arquivo `.env` na pasta `backend` com:**
```env
GOOGLE_API_KEY=SUA_CHAVE_AQUI
GEMINI_MODEL=gemini-3.8-flash
```

⚠️ **Importante:** Substitua `SUA_CHAVE_AQUI` pela sua chave real do Google AI Studio. Nunca compartilhe ou commit este arquivo.

**6. Rode o servidor:**
```powershell
uvicorn main:app --reload
```

✅ Backend rodando em: **http://127.0.0.1:8000**

📖 Documentação da API: **http://127.0.0.1:8000/docs**

---

### Passo 3: Configurar o Frontend

**Abra um NOVO terminal (mantenha o backend rodando!)**

**1. Navegue até a pasta do frontend:**
```powershell
cd caminho/para/studyia/frontend
```

**2. Instale as dependências:**
```powershell
npm install
```

**3. Rode no navegador:**
```powershell
npx expo start --web
```

✅ Frontend rodando em: **http://localhost:19006**

---

### Acessar o Sistema

- **Frontend (Aplicação):** http://localhost:19006
- **Backend API:** http://127.0.0.1:8000
- **Documentação Swagger:** http://127.0.0.1:8000/docs

---

## 📡 Tabela de Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/` | Verifica se a API está funcionando |
| GET | `/health` | Health check para monitoramento |
| GET | `/opcoes` | Retorna níveis e tipos permitidos |
| POST | `/estudo` | Gera conteúdo de estudo usando Gemini |

---

## 📝 Exemplo Real de Requisição e Resposta

### Requisição (POST /estudo)

```json
{
  "materia": "Biologia",
  "assunto": "Fotossíntese",
  "nivel": "iniciante",
  "tipo": "explicacao"
}
```

### Resposta de Sucesso (200)

```json
{
  "materia": "Biologia",
  "assunto": "Fotossíntese",
  "nivel": "iniciante",
  "tipo": "explicacao",
  "resposta": "A fotossíntese é o processo pelo qual as plantas produzem seu próprio alimento..."
}
```

### Resposta de Erro (422 - Validação)

```json
{
  "erro": "O assunto é obrigatório e deve ter entre 3 e 150 caracteres."
}
```

### Resposta de Erro (429 - Limite de Uso)

```json
{
  "erro": "Muitas requisições. Tente novamente em instantes."
}
```

---

## 🔗 Integração com a API Gemini

### Fluxo Completo

1. **Usuário preenche formulário**
   - Matéria, assunto, nível, tipo

2. **Frontend envia requisição**
   - POST `/estudo` com dados em JSON

3. **Backend valida dados**
   - Pydantic verifica formato e tamanho
   - Regras de negócio verificam conteúdo

4. **Backend gera prompt**
   - Sistema seleciona template baseado no tipo
   - Prompt é personalizado com nível e assunto

5. **GeminiService chama API**
   - Envia prompt para modelo gemini-3.8-flash
   - Chave API fica segura no backend (.env)

6. **Gemini processa e responde**
   - IA gera conteúdo educacional
   - Resposta em português do Brasil

7. **Backend formata resposta**
   - Retorna JSON com dados + resposta gerada

8. **Frontend exibe resultado**
   - Tela de resultado mostra conteúdo
   - Scroll para respostas longas

### Exemplo de Prompt Gerado

**Tipo: Explicação | Nível: Iniciante**

```
Você é um professor paciente. Explique sobre 'Fotossíntese' na matéria 'Biologia' 
para um nível iniciante (alguém que está começando a aprender).

Siga estas instruções:
- Explique de forma clara e didática
- Use exemplos práticos do dia a dia
- Evite jargões técnicos sem explicação
- A resposta deve ter cerca de 200-300 palavras
- Responda em português do Brasil
```

---

## ✅ Regras de Negócio e Validações

### Validações de Campos (Pydantic)

| Campo | Regras |
|-------|--------|
| `materia` | Obrigatório, 2-80 caracteres, não pode ser apenas espaços |
| `assunto` | Obrigatório, 3-150 caracteres, não pode ser apenas espaços |
| `nivel` | Obrigatório, deve ser: `iniciante`, `intermediario` ou `avancado` |
| `tipo` | Obrigatório, deve ser: `explicacao`, `resumo`, `quiz` ou `perguntas` |

### Validações de Negócio

1. **Normalização:** Espaços extras são removidos do início e fim. `nivel` e `tipo` são convertidos para minúsculas.
2. **Assuntos bloqueados:** Termos considerados perigosos ou ofensivos são rejeitados (ex: "como fazer bomba", "como hackear").
3. **Limite de conteúdo:** Quiz tem 5 questões, perguntas tem 5 itens.

### Tipos de Conteúdo

| Tipo | Descrição |
|------|-----------|
| `explicacao` | Explicação didática com exemplos práticos (200-300 palavras) |
| `resumo` | Resumo em tópicos com 5-7 pontos principais |
| `quiz` | 5 questões de múltipla escolha com gabarito e justificativa |
| `perguntas` | 5 perguntas de estudo/revisão sem respostas |

---

## 🚨 Tratamento de Erros

| Código HTTP | Significado | Mensagem |
|-------------|-------------|----------|
| 200 | Sucesso | Conteúdo gerado com sucesso |
| 400 | Requisição inválida | Assunto não permitido |
| 422 | Validação falhou | Dados inválidos (formato, tamanho, valores) |
| 429 | Muitas requisições | Limite de uso do Gemini atingido |
| 500 | Erro interno | Serviço de IA não configurado |
| 502 | Bad Gateway | Não foi possível gerar o conteúdo |

**Formato padrão de erro:**
```json
{
  "erro": "Mensagem descritiva em português"
}
```

---

## 🧪 Demonstração do Sistema

### Cenário de Uso Completo

**1. Usuário abre o aplicativo**
   - Acessa http://localhost:19006
   - Vê tela de formulário do StudyIA

**2. Preenche os dados**
   - Matéria: "Estrutura de Dados"
   - Assunto: "Árvores Binárias"
   - Nível: "Intermediário"
   - Tipo: "Explicação"

**3. Clica em "Gerar Conteúdo"**
   - Frontend mostra indicador de carregamento
   - Requisição é enviada ao backend

**4. Backend processa**
   - Valida os dados
   - Gera prompt específico
   - Chama API Gemini
   - Recebe resposta

**5. Usuário vê resultado**
   - Tela de resultado aparece
   - Explicação detalhada é exibida
   - Pode fazer nova consulta

### Outros Cenários de Teste

**Teste de Validação:**
- Deixar campo "Assunto" vazio
- Sistema mostra alerta: "O assunto é obrigatório"

**Teste de Quiz:**
- Tipo: "Quiz"
- Sistema gera 5 questões com gabarito

**Teste de Resumo:**
- Tipo: "Resumo"
- Sistema gera tópicos principais

---

## 📁 Estrutura de Pastas

```
studyia/
├── backend/
│   ├── main.py              # API FastAPI com endpoints
│   ├── models.py            # Schemas Pydantic (validação)
│   ├── prompts.py           # Templates de prompt por tipo
│   ├── gemini_service.py    # Integração com API Gemini
│   ├── requirements.txt     # Dependências Python
│   ├── .env.example         # Exemplo de configuração
│   ├── .gitignore           # Arquivos a ignorar no Git
│   └── .env                 # Variáveis de ambiente (NÃO commitar)
├── frontend/
│   ├── App.js               # Componente principal (telas)
│   ├── config.js            # Configuração da URL da API
│   ├── package.json         # Dependências do projeto
│   ├── app.json             # Configuração do Expo
│   ├── babel.config.js      # Configuração do Babel
│   └── .gitignore           # Arquivos a ignorar no Git
└── README.md                # Este arquivo
```

---

## 🔒 Segurança

### Proteção da Chave API

- **Chave da API:** A chave do Gemini fica SOMENTE no backend (arquivo `.env`). NUNCA no frontend.
- **Arquivo .env:** O `.env` está no `.gitignore` para não ser commitado no Git.
- **Variável de ambiente:** Chave é carregada via `python-dotenv` e nunca é logada.

### Outras Medidas de Segurança

- **CORS:** Configurado para permitir requisições do frontend. Em produção, deve ser restrito a origens específicas.
- **Validação de entrada:** Todos os dados são validados antes de serem processados.
- **Assuntos bloqueados:** Lista de termos considerados perigosos é verificada antes de chamar o Gemini.
- **Logging:** Erros são registrados sem expor informações sensíveis (chaves, senhas).

---

## 🎨 Funcionalidades do Frontend

### Tela de Formulário
- ✅ Campo "Matéria" (limite 80 caracteres)
- ✅ Campo "Assunto" (limite 150 caracteres)
- ✅ Seletor de "Nível" (Iniciante, Intermediário, Avançado)
- ✅ Seletor de "Tipo" (Explicação, Resumo, Quiz, Perguntas)
- ✅ Validação no frontend antes de enviar
- ✅ Indicador de carregamento durante requisição
- ✅ Mensagens de erro em caixa vermelha
- ✅ Botão desabilitado durante carregamento
- ✅ Carregamento automático de opções da API

### Tela de Resultado
- ✅ Mostra matéria, assunto, nível e tipo
- ✅ Exibe o conteúdo gerado pelo Gemini
- ✅ Scroll para respostas longas
- ✅ Botão "Nova Consulta" para retornar ao formulário

### Design
- ✅ Cor principal: Roxo (#6366f1)
- ✅ Fundo claro com cartão central
- ✅ Layout responsivo (funciona em navegador e celular)
- ✅ Componentes nativos do React Native
- ✅ Interface simples e intuitiva

---

## ❓ Problemas Comuns e Soluções

### Backend

#### Problema: "GOOGLE_API_KEY não configurada"
**Causa:** Arquivo `.env` não criado ou chave não preenchida.
**Solução:** Crie o arquivo `.env` com sua chave real e reinicie o servidor.

#### Problema: "python não é reconhecido"
**Causa:** Python não está instalado ou não está no PATH.
**Solução:** Instale Python 3.10+ em https://python.org e marque "Add Python to PATH" durante a instalação.

#### Problema: "Module not found"
**Causa:** Ambiente virtual não ativado ou dependências não instaladas.
**Solução:** Ative o venv (`.\venv\Scripts\activate`) e rode `pip install -r requirements.txt`.

#### Problema: Erro 429 "Muitas requisições"
**Causa:** Limite de uso da API Gemini atingido.
**Solução:** Espere alguns minutos e tente novamente. Verifique seus limites no Google AI Studio.

#### Problema: Erro 502 "Não foi possível gerar o conteúdo"
**Causa:** Serviço Gemini fora do ar, timeout ou resposta vazia.
**Solução:** Verifique sua conexão e tente novamente. Se persistir, verifique o status do Google AI Studio.

---

### Frontend

#### Problema: "npm não é reconhecido"
**Causa:** Node.js não está instalado ou não está no PATH.
**Solução:** Instale Node.js 18+ em https://nodejs.org/

#### Problema: "Network request failed"
**Causa:** Backend não está rodando ou URL errada no `config.js`.
**Solução:** Verifique se o backend está rodando em `http://127.0.0.1:8000` e se a URL em `frontend/config.js` está correta.

#### Problema: Porta 19006 já em uso
**Causa:** Outro processo usando a porta.
**Solução:** Feche outros projetos Expo ou use `npx expo start --web --port 19007`

#### Problema: Tela branca
**Causa:** Erro de JavaScript.
**Solução:** Abra o console do navegador (F12) para ver o erro detalhado.

---

### Integração

#### Problema: CORS bloqueando requisições
**Causa:** Frontend tentando acessar de origem não permitida.
**Solução:** Verifique se o middleware CORS está configurado no `backend/main.py`.

#### Problema: Frontend não conecta ao backend
**Causa:** Backend não está rodando ou URL incorreta.
**Solução:** 
1. Verifique se o backend está rodando (terminal 1)
2. Teste http://127.0.0.1:8000/docs no navegador
3. Verifique a URL em `frontend/config.js`

---

## 🎓 Contexto Acadêmico

Este projeto foi desenvolvido como trabalho acadêmico para demonstrar:
- ✅ Integração entre frontend (React Native) e backend (FastAPI)
- ✅ Uso de APIs de IA generativa (Google Gemini)
- ✅ Validação de dados e regras de negócio (Pydantic)
- ✅ Boas práticas de segurança (chave no backend, CORS)
- ✅ Documentação técnica completa
- ✅ Tratamento de erros amigável
- ✅ Design responsivo e intuitivo

---

## 📚 Documentação Adicional

### Backend
- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) - Documentação interativa Swagger (requer backend rodando)

---

## 🎯 Próximos Passos

- [ ] Testar o sistema completo (backend + frontend)
- [ ] (Opcional) Deploy em nuvem (Render, Railway, etc.)

---

## 📝 Licença

Este projeto está sob a licença **MIT**. Sinta-se à vontade para usar, modificar e compartilhar.

---

## 👨‍💻 Desenvolvido por

[Seu Nome] - [Sua Instituição]

---

## 📞 Suporte

Para dúvidas ou problemas, consulte a documentação do [FastAPI](https://fastapi.tiangolo.com/) e do [Google AI](https://ai.google.dev/docs).
