from fastapi import APIRouter
from.endpoints import licitacoes, login, users # Adicionar users

api_router = APIRouter()
api_router.include_router(login.router, prefix="/login", tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"]) # Adicionar rota de users
api_router.include_router(licitacoes.router, prefix="/licitacoes", tags=["licitacoes"])