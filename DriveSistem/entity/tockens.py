import os
import secrets
from datetime import datetime, timedelta
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
import jwt
from pydantic import BaseModel
from starlette import status

SECRET_KEY = os.getenv('JWT_SECRET_KEY', secrets.token_hex(32))
ALGORITHM = 'HS256'

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Token(BaseModel):
    access_token: str
    token_type: str
def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=15)):
    """ Создание JWT-токена """
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(token: str = Depends(oauth2_scheme), user_repository):
    """ Декодирование токена и получение пользователя """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        role: str = payload.get("role")
        if email is None or role is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = user_repository.get_user(email)
    if user is None:
        raise credentials_exception
    return {"email": user["email"], "name": user["name"], "role": role}