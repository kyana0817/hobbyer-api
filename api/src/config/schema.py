from datetime import datetime
from sqlalchemy import ( Column, Integer,
String, Text, Boolean, DateTime, ForeignKey)
from sqlalchemy.orm import relationship

from app.infrastractures.database import Base

class UserHobby(Base):
  __tablename__ = 'user_hobbies'
  
  user_id = Column(ForeignKey('users.id'), primary_key=True, nullable=False)
  hobby_id = Column(ForeignKey('hobbies.id'), primary_key=True, nullable=False)


class User(Base):
  __tablename__ = 'users'
  
  id = Column(Integer, primary_key=True, autoincrement=True)
  username = Column(String(length=255), nullable=False)
  email = Column(String(length=255), nullable=False, index=True, unique=True)
  self_intro = Column(Text)
  avater = Column(String(length=255))
  is_match = Column(Boolean, default=True)
  created_at = Column(DateTime, default=datetime.now, nullable=False)
  updated_at = Column(DateTime, default=None, onupdate=datetime.now)
  deleted_at = Column(DateTime, default=None)

  hobbies = relationship('Hobby', secondary=UserHobby.__tablename__)
  # circles = relationship('UserCircle', back_populates='circle')
  # chats = relationship('CircleChat', back_populates='user')


class Hobby(Base):
  __tablename__ = 'hobbies'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(length=64), nullable=False)
  description = Column(Text)
  created_at = Column(DateTime, default=datetime.now, nullable=False)
  updated_at = Column(DateTime, default=None, onupdate=datetime.now)
  deleted_at = Column(DateTime, default=None)
  
  users = relationship('User', secondary=UserHobby.__tablename__)


# class Circle(Base):
#   __tablename__ = 'circles'

#   id = Column(Integer, primary_key=True)
#   name = Column(String(length=64), nullable=False)
#   description = Column(Text)
#   created_at = Column(DateTime, default=datetime.now, nullable=False)
#   updated_at = Column(DateTime, default=None, onupdate=datetime.now)
#   deleted_at = Column(DateTime, default=None)

#   users = relationship('UserCircle', back_populates='user')
#   chats = relationship('CircleChat', back_populates='circle')




# class UserCircle(Base):
#   __tablename__ = 'user_circles'
  
#   user_id = Column(ForeignKey('users.id'), primary_key=True, nullable=False)
#   circle_id = Column(ForeignKey('circles.id'), primary_key=True, nullable=False)

#   user = relationship('User', back_populates='circles')
#   circle = relationship('Hobby', back_populates='users')


# class CircleChat(Base):
#   __tablename__ = 'circle_chats'

#   id = Column(Integer, primary_key=True, autoincrement=True)
#   user_id = Column(ForeignKey('users.id'), nullable=False)
#   circle_id = Column(ForeignKey('circles.id'), nullable=False)
#   message = Column(Text, nullable=False)
#   sent_datetime = Column(DateTime, default=datetime.now, nullable=False)
#   created_at = Column(DateTime, default=datetime.now, nullable=False)
#   updated_at = Column(DateTime, default=None, onupdate=datetime.now)
#   deleted_at = Column(DateTime, default=None)

#   user = relationship('User', back_populates='chats')
#   circle = relationship('Circle', back_populates='chats')


# class PrivateChat(Base):
#   __tablename__ = 'private_chats'

#   id = Column(Integer, primary_key=True, autoincrement=True)
#   sent_user_id = Column(ForeignKey('users.id'), nullable=False)
#   reception_user_id = Column(ForeignKey('users.id'), nullable=False)
#   message = Column(Text, nullable=False)
#   sent_datetime = Column(DateTime, default=datetime.now, nullable=False)
#   created_at = Column(DateTime, default=datetime.now, nullable=False)
#   updated_at = Column(DateTime, default=None, onupdate=datetime.now)
#   deleted_at = Column(DateTime, default=None)

#   sent_user = relationship('User', back_populates='private_senders')
#   reception_user = relationship('User', back_populates='private_recepters')

# class FriendshipStatus(Base):
#   __tablename__ = 'friendship_statuses'

#   id = Column(Integer, primary_key=True, autoincrement=True)
#   status = Column(Boolean, default=False)
#   created_at = Column(DateTime, default=datetime.now, nullable=False)
#   updated_at = Column(DateTime, default=None, onupdate=datetime.now)
#   deleted_at = Column(DateTime, default=None)

# class Friendships(Base):
#   __tablename__ = 'friendships'
  
#   target_id = Column(ForeignKey('users.id'), primary_key=True, nullable=False)
#   source_id = Column(ForeignKey('users.id'), primary_key=True, nullable=False)
#   friendship_status_id = Column(ForeignKey('friendship_statuses.id'), nullable=False)
