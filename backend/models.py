from pydantic import BaseModel, Field, field_validator
from typing import Literal


class EstudoRequest(BaseModel):
    """Modelo da requisição para o endpoint /estudo"""
    materia: str = Field(..., min_length=2, max_length=80, description="Nome da matéria")
    assunto: str = Field(..., min_length=3, max_length=150, description="Assunto a ser estudado")
    nivel: Literal["iniciante", "intermediario", "avancado"] = Field(..., description="Nível de estudo")
    tipo: Literal["explicacao", "resumo", "quiz", "perguntas"] = Field(..., description="Tipo de conteúdo desejado")

    @field_validator('materia')
    @classmethod
    def materia_nao_vazia(cls, v: str) -> str:
        """Valida que a matéria não seja apenas espaços"""
        if not v or v.strip() == "":
            raise ValueError("A matéria é obrigatória.")
        return v.strip()

    @field_validator('assunto')
    @classmethod
    def assunto_nao_vazio(cls, v: str) -> str:
        """Valida que o assunto não seja apenas espaços"""
        if not v or v.strip() == "":
            raise ValueError("O assunto é obrigatório.")
        return v.strip()

    @field_validator('nivel', 'tipo')
    @classmethod
    def normalizar_minusculas(cls, v: str) -> str:
        """Normaliza nivel e tipo para minúsculas"""
        return v.lower()


class EstudoResponse(BaseModel):
    """Modelo da resposta do endpoint /estudo"""
    materia: str
    assunto: str
    nivel: str
    tipo: str
    resposta: str


class ErrorResponse(BaseModel):
    """Modelo padrão de erro"""
    erro: str


class OpcoesResponse(BaseModel):
    """Modelo da resposta do endpoint /opcoes"""
    niveis: list[str]
    tipos: list[str]
