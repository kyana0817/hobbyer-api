from sqlalchemy.orm import Session

from app.config.schema import User
from app.models.user import UserCreate


def user_create(db: Session, data: UserCreate):
  user = User(username=data.username, email=data.email)
  db.add(user)
  db.commit()
  db.refresh(user)
  return user

def user_info(db: Session, id):
  return db.query(User).filter(User.id == id).first()
  