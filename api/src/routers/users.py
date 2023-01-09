from fastapi import APIRouter, Depends, Request

from app.dependencies import get_db, get_current_user

router = APIRouter(
  prefix="/user",
  dependencies=[Depends(get_db), Depends(get_current_user)]
)


@router.get("/")
def read_item(request: Request):
  return {'asdasdaoi': 'dsaodadoadso'}
