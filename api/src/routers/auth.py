from fastapi import APIRouter, Header, Request

from app.infrastractures.authenticate import set_custom_field, get_auth
from app.handlers.authHandlers import user_create, user_info
from app.models.user import UserCreate

router = APIRouter(
  prefix="/auth"
)

@router.get('/temp')
def temp(test):
  print(test)
  return {'hello': 'world'}

@router.post('/register')
def user_registration(request: Request, body: UserCreate, authorization: str | None = Header(default=None)):
  user = user_create(request.state.db, body)
  current_user = get_auth(authorization)
  set_custom_field(current_user, user.id)

  return True

@router.get('/current_user')
def current_user(request: Request):
  return user_info(request.state.db, request.state.current_user)