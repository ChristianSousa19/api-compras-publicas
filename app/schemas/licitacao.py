from pydantic import BaseModel
from datetime import date
from typing import List, Optional

# Schemas de Fornecedor
class FornecedorBase(BaseModel):
    cnpj: str
    nome: str

class FornecedorCreate(FornecedorBase):
    pass

class Fornecedor(FornecedorBase):
    class Config:
        from_attributes = True

# Schemas de Contrato
class ContratoBase(BaseModel):
    numero_contrato: str
    valor_inicial: float
    data_assinatura: date

class ContratoCreate(ContratoBase):
    licitacao_id: int
    fornecedor_cnpj: str

class Contrato(ContratoBase):
    id: int
    licitacao_id: int
    fornecedor: Fornecedor

    class Config:
        from_attributes = True

# Schemas de Licitação
class LicitacaoBase(BaseModel):
    numero_licitacao: str
    objeto: str
    data_publicacao: date

class LicitacaoCreate(LicitacaoBase):
    pass

class Licitacao(LicitacaoBase):
    id: int
    contratos: List[Contrato] = []          # lista vazia como default
    fornecedores: List[Fornecedor] = []     # lista vazia como default

    class Config:
        from_attributes = True

# Schemas de Usuário e Autenticação
class UserBase(BaseModel):
    username: str
    role: str

class UserCreate(BaseModel):
    username: str
    password: str
    role: str = "leitor"

class User(UserBase):
    id: int
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None