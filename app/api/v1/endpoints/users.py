from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud import crud_licitacao as crud
from app.schemas import licitacao as schemas
from app.core.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_user(
    *,
    db: Session = Depends(get_db),
    user_in: schemas.UserCreate,
):
    """
    Cria um novo usuário no sistema.
    """
    user = crud.user.get_by_username(db, username=user_in.username)
    if user:
        raise HTTPException(
            status_code=400,
            detail="Um usuário com este nome de usuário já existe.",
        )
    user = crud.user.create(db=db, obj_in=user_in)
    return user