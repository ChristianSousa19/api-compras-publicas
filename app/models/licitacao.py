from sqlalchemy import (Column, Integer, String, Date, Numeric, ForeignKey, Table)
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List
from datetime import date

from app.core.database import Base

# Tabela de Associação para a relação N:N entre Licitacao e Fornecedor
licitacao_fornecedor_association = Table(
    'licitacao_fornecedor', Base.metadata,
    Column('licitacao_id', Integer, ForeignKey('licitacoes.id'), primary_key=True),
    Column('fornecedor_cnpj', String, ForeignKey('fornecedores.cnpj'), primary_key=True)
)

class Licitacao(Base):
    __tablename__ = "licitacoes"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    numero_licitacao: Mapped[str] = mapped_column(String, unique=True, index=True)
    objeto: Mapped[str] = mapped_column(String)
    # CORREÇÃO: O tipo 'date' foi adicionado dentro de Mapped
    data_publicacao: Mapped[date] = mapped_column(Date)
    
    contratos: Mapped[List["Contrato"]] = relationship(back_populates="licitacao")
    fornecedores: Mapped[List["Fornecedor"]] = relationship(
        secondary=licitacao_fornecedor_association, back_populates="licitacoes"
    )

class Contrato(Base):
    __tablename__ = "contratos"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    numero_contrato: Mapped[str] = mapped_column(String, unique=True, index=True)
    valor_inicial: Mapped[float] = mapped_column(Numeric(15, 2))
    # CORREÇÃO: O tipo 'date' foi adicionado dentro de Mapped
    data_assinatura: Mapped[date] = mapped_column(Date)
    
    licitacao_id: Mapped[int] = mapped_column(ForeignKey("licitacoes.id"))
    licitacao: Mapped["Licitacao"] = relationship(back_populates="contratos")
    
    fornecedor_cnpj: Mapped[str] = mapped_column(ForeignKey("fornecedores.cnpj"))
    fornecedor: Mapped["Fornecedor"] = relationship(back_populates="contratos")

class Fornecedor(Base):
    __tablename__ = "fornecedores"
    cnpj: Mapped[str] = mapped_column(String(14), primary_key=True, index=True)
    nome: Mapped[str] = mapped_column(String, index=True)
    
    contratos: Mapped[List["Contrato"]] = relationship(back_populates="fornecedor")
    licitacoes: Mapped[List["Licitacao"]] = relationship(
        secondary=licitacao_fornecedor_association, back_populates="fornecedores"
    )

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String)
    role: Mapped[str] = mapped_column(String, default="leitor")