import os
import sys
from pathlib import Path

# Adiciona o diretório raiz do projeto ao sys.path
# para que o alembic possa encontrar o módulo 'app'
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# Importe sua Base e os modelos para que o Alembic os reconheça
from app.core.database import Base
from app.models.licitacao import * # noqa

# esta é a configuração do Alembic, que fornece
# acesso aos valores dentro do arquivo.ini em uso.
config = context.config

# Interprete o arquivo de configuração para o logging do Python.
# Esta linha configura basicamente os loggers.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# adicione o objeto MetaData do seu modelo aqui
# para suporte a 'autogenerate'
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Executa as migrações no modo 'offline'."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Executa as migrações no modo 'online'."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()