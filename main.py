from fastapi import FastAPI
from app.api.v1.router import api_router
from app.core.database import Base, engine

# Cria as tabelas no banco de dados (para desenvolvimento)
# Em produção, você usaria Alembic para gerenciar as migrações
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Compras Públicas",
    description="API para consulta de dados de licitações e contratos do governo.",
    version="1.0.0"
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Compras Públicas"}