from fastapi import APIRouter, Header, Depends, Request

from app.infrastractures.authenticate import set_custom_field, get_auth
from app.handlers.authHandlers import user_create
from app.dependencies import get_db, get_current_user
from app.models.user import UserCreate

router = APIRouter(
  prefix="/user",
  dependencies=[Depends(get_db), Depends(get_current_user)]
)


@router.get("/")
def read_item(request: Request):
  print(request.state.current_user)
  return {'asdasdaoi': 'dsaodadoadso'}

