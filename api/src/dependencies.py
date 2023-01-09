from fastapi import Request, Header

from app.infrastructures.authenticate import get_auth, current_user
from app.infrastructures.database import SessionLocal

def get_db(request: Request):
  request.state.db = SessionLocal()
  try:
    yield request.state.db
  finally:
    request.state.db.close()

def get_current_user(request: Request, authorization: str | None = Header(default=None)):
  request.state.current_user = None

  if authorization is not None:
    user = get_auth(authorization)
    request.state.current_user = current_user(user)

  return request
