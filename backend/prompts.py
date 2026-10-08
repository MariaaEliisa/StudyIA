def gerar_prompt(materia: str, assunto: str, nivel: str, tipo: str) -> str:
    """
    Gera o prompt apropriado para o Gemini baseado no tipo de conteúdo solicitado.
    """
    nivel_por_extenso = {
        "iniciante": "iniciante (alguém que está começando a aprender)",
        "intermediario": "intermediário (já tem conhecimento básico)",
        "avancado": "avançado (tem domínio do assunto)"
    }
    
    nivel_desc = nivel_por_extenso.get(nivel, nivel)
    
    base_intro = f"Você é um professor paciente. Explique sobre '{assunto}' na matéria '{materia}' para um nível {nivel_desc}."
    
    if tipo == "explicacao":
        return f"""{base_intro}
        
Siga estas instruções:
- Explique de forma clara e didática
- Use exemplos práticos do dia a dia
- Evite jargões técnicos sem explicação
- A resposta deve ter cerca de 200-300 palavras
- Responda em português do Brasil"""
    
    elif tipo == "resumo":
        return f"""{base_intro}
        
Siga estas instruções:
- Faça um resumo em tópicos curtos
- Liste os 5-7 pontos principais do assunto
- Seja direto e objetivo
- Use Markdown com marcadores (• ou -)
- Responda em português do Brasil"""
    
    elif tipo == "quiz":
        return f"""{base_intro}
        
Siga estas instruções:
- Crie 5 questões de múltipla escolha (A, B, C, D)
- Cada questão deve testar um aspecto diferente do assunto
- Após cada questão, indique a resposta correta
- Adicione uma breve justificativa (1-2 linhas) para cada resposta
- As questões devem ser adequadas ao nível {nivel_desc}
- Use formato markdown para estruturação
- Responda em português do Brasil"""
    
    elif tipo == "perguntas":
        return f"""{base_intro}
        
Siga estas instruções:
- Crie 5 perguntas de estudo/revisão
- As perguntas devem estimular reflexão e fixação do conteúdo
- Ordene as perguntas do mais fácil para o mais difícil
- NÃO forneça as respostas (apenas as perguntas)
- As perguntas devem ser adequadas ao nível {nivel_desc}
- Use formato markdown com numeração
- Responda em português do Brasil"""
    
    else:
        return f"{base_intro} Explique o assunto de forma geral."
