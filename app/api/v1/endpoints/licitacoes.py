from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud import crud_licitacao
from app.schemas import licitacao as licitacao_schema
from app.core.database import get_db
from app.api.v1.dependencies import get_current_user, RoleChecker
from app.models.licitacao import User as UserModel

router = APIRouter()

# --- CORREÇÃO DEFINITIVA ---
# A sintaxe correta para a dependência é uma lista contendo a chamada
# 'Depends' que, por sua vez, instancia a classe RoleChecker.
@router.post(
    "/",
    response_model=licitacao_schema.Licitacao,
    dependencies=[Depends(RoleChecker(["admin"]))]  # <<< CORRETO
)
def create_licitacao(
    *,
    db: Session = Depends(get_db),
    licitacao_in: licitacao_schema.LicitacaoCreate,
    current_user: UserModel = Depends(get_current_user)
):
    """
    Cria uma nova licitação. Requer privilégios de administrador.
    """
    return crud_licitacao.licitacao.create(db=db, obj_in=licitacao_in)


# Exemplo de rota pública (sem alterações)
@router.get("/", response_model=List[licitacao_schema.Licitacao])
def read_licitacoes(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
):
    """
    Retorna uma lista de licitações com paginação.
    """
    licitacoes = crud_licitacao.licitacao.get_multi(db, skip=skip, limit=limit)
    return licitacoes
