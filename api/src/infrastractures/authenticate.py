import firebase_admin
from firebase_admin import auth, credentials

from app.config import path

cred = credentials.Certificate(f'{path}/FirebaseAccessKey.json')
firebase_admin.initialize_app(cred)

def get_auth(token):
  cleand = clean_token(token)
  decoded = auth.verify_id_token(cleand)
  user = auth.get_user(decoded['uid'])
  return user

def set_custom_field(user, appid):
  auth.set_custom_user_claims(user.uid, {'appid': appid})

def clean_token(token):
  return token.replace('Bearer ', '')

def current_user(user):
  return user.custom_claims.get('appid')