import os
import secrets
from datetime import datetime, timedelta
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
import jwt
from starlette import status
import uvicorn

from entity.tockens import Token
from registerSistem.registration.send_email import MailSender
from entity.user import UserContacts
from registerSistem.registration.repository.user_repository import UserRepository
from registerSistem.registration.repository.user_repository_approve import UserRepositoryApprove

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



@app.post("/register/", tags=["Registration"])
def register_as_user(user: UserContacts):
    if user_repository.is_user_registered(user):
        raise HTTPException(status_code=400, detail=f"User {user.email} already registered")
    approve_code = 1
    user_repository_redis.add_user(approve_code, user)
    mail_sender.send_mail(user.email, approve_code)
    return {"status": "success", "message": "Mail sent successfully"}


@app.post("/register/approve", tags=["Approval"])
def approve_user(approve_code: int):
    user = user_repository_redis.get_user_by_code(approve_code)
    if not user:
        raise HTTPException(status_code=404, detail="The confirmation period has expired")
    user_repository.add_user(user)
    return {"status": "success", "message": "You are registered"}
@app.post("/login/", response_model=Token, tags=["Authentication"])
def login_user(creds: UserContacts):
    if not user_repository.is_user_found(creds):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(data={"sub": creds.email, "role": creds.role})
    return {"access_token": token, "token_type": "bearer"}


def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=15)):
    """ Создание JWT-токена """
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(token: str = Depends(oauth2_scheme)):
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


@app.get("/admin")
async def admin_route(current_user: UserContacts = Depends(get_current_user)):
    """ Эндпоинт доступен только администраторам """
    if current_user.role != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied")
    return {"message": f"Welcome, {current_user.name}! You have admin access."}


@app.get("/protected")
async def protected_route(current_user: UserContacts = Depends(get_current_user)):
    """ Эндпоинт доступен всем авторизованным пользователям """
    return {"message": f"Hello, {current_user.name}! Your role is {current_user.role}."}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8003)




