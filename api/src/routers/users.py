from fastapi import APIRouter, Header, Depends, Request
from sqlalchemy.orm import Session

from app.infrastractures.database import get_db
from app.infrastractures.authenticate import set_custom_field, get_auth
from app.handlers.authHandlers import user_create
from app.models.user import UserCreate

router = APIRouter(
  prefix="/user"
)


@router.get("/")
def read_item(request: Request):
  print(request.state.current_user)
  return {'asdasdaoi': 'dsaodadoadso'}

