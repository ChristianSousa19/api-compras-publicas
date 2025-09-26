from sqlalchemy.orm import Session
from.base import CRUDBase
from app.models.licitacao import Licitacao, User
from app.schemas.licitacao import LicitacaoCreate, UserCreate
from app.core.security import get_password_hash

class CRUDLicitacao(CRUDBase[Licitacao, LicitacaoCreate, LicitacaoCreate]):
    pass

class CRUDUser(CRUDBase[User, UserCreate, UserCreate]):
    def get_by_username(self, db: Session, *, username: str) -> User:
        return db.query(User).filter(User.username == username).first()

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        db_obj = User(
            username=obj_in.username,
            hashed_password=get_password_hash(obj_in.password),
            role=obj_in.role,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

licitacao = CRUDLicitacao(Licitacao)
user = CRUDUser(User)