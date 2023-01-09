from fastapi import APIRouter, Request, Depends, Header

from app.infrastructures.authenticate import set_custom_field, get_auth
from app.dependencies import get_current_user, get_db
from app.handlers import auth as auth_handler
from app.models.user import UserCreate

router = APIRouter(
  prefix="/auth",
  dependencies=[Depends(get_db)]
)


@router.post('/register')
def user_registration(request: Request, body: UserCreate, authorization: str | None = Header(default=None)):
  user = get_auth(authorization)
  db_user = auth_handler.user_create(request.state.db, body)

  set_custom_field(user, db_user.id)

  return db_user

@router.get('/current_user', dependencies=[Depends(get_current_user)])
def current_user(request: Request):
  return auth_handler.user_info(request.state.db, request.state.current_user)
  