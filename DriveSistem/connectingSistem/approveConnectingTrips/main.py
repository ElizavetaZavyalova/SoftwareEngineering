import os
import secrets
from datetime import datetime, timedelta
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
import jwt
from pydantic import BaseModel
from starlette import status
import uvicorn

from entity.tockens import get_current_user
from registerSistem.registration.send_email import MailSender
from entity.user import UserContacts
from registerSistem.registration.repository.user_repository import UserRepository
from registerSistem.registration.repository.user_repository_approve import UserRepositoryApprove
from authx import AuthXConfig, AuthX

app = FastAPI(
    title="Registration System API",
    description="API для регистрации и авторизации пользователей и водителей",
    version="1.0",
    docs_url="/docs",
    openapi_url="/openapi.json"
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

user_repository_redis = UserRepositoryApprove()
user_repository = UserRepository()
mail_sender = MailSender()
SECRET_KEY = os.getenv('JWT_SECRET_KEY', secrets.token_hex(32))  # Use environment variable or fallback to a secure random key
ALGORITHM = 'HS256'

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
@app.get("/protected")
async def protected_route(current_user: UserContacts = Depends(get_current_user)):
    """ Эндпоинт доступен всем авторизованным пользователям """
    return {"message": f"Hello, {current_user.name}! Your role is {current_user.role}."}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8004)
