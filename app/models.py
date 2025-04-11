from pydantic import BaseModel
from typing import Optional, List, Dict

class ClientePerfil(BaseModel):
    nome: str
    telefone: str
    nome_completo: Optional[str] = None
    profissao: Optional[str] = None
    redes_sociais: Optional[Dict[str, str]] = None
    interesses: Optional[List[str]] = None
    mencoes: Optional[List[str]] = None
    imagens: Optional[List[str]] = None
    inferencias: Optional[Dict[str, str]] = None
