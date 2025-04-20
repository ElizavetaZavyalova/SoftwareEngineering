import os

import uvicorn
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from starlette.responses import JSONResponse

from libs.email.entity.email_confirmation import EmailConfirmation
from libs.tocken_generator.entity.account import Account
from passenger.account_sistem.controller.controller import Controller, Tags
from passenger.passenger.rest.passenger import Passenger
from passenger.passenger_repository.rdbms import PassengerRepositoryRDBMS
from passenger.passenger_repository.redis import PassengerRepositoryRedis

app = FastAPI(
    title="FastAPI Token Authentication",
    description="API для ригестрации пассажира",
    version="1.0",
    docs_url="/docs"
)
redis_repository = PassengerRepositoryRedis()
account_repository = PassengerRepositoryRDBMS(
    url=os.getenv("DATABASE_PASSENGER_URL", "postgresql://root:root@localhost:5502/passengers"))
controller = Controller(redis=redis_repository, rdbms=account_repository)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/health", tags=["Health"])
async def healthcheck():
    return JSONResponse(content={"status": "ok"})
@app.post("/token", tags=[Tags._LOG_IN],
        summary="Получение токена")
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return controller.login(Account(email=form_data.username, password=form_data.password))


# # # # # #
@app.post('/passenger/register/', tags=[Tags._REGISTER],
        summary="Регистрация пассажира")
async def register_passenger(passenger: Passenger):
    return controller.register_user(user=passenger)


@app.post('/passenger/confirm/email/', tags=[Tags._REGISTER],
        summary="Подтверждения email")
async def confirm_email_passenger(email_confirmation: EmailConfirmation):
    return controller.confirm_email(email_confirmation=email_confirmation)


@app.post('/passenger/forgot/password/', tags=[Tags._PASSWORD_RECOVERY],
        summary="Востановление пароля")
async def forgot_password(account: Account):
    return controller.forgot_password(account=account)


@app.post('/passenger/change/password/', tags=[Tags._PASSWORD_RECOVERY],
        summary="Подтверждения нового пароля")
async def change_password(email_confirmation: EmailConfirmation):
    return controller.change_password(email_confirmation=email_confirmation)


@app.post("/passenger/login", tags=[Tags._LOG_IN],
        summary="Вход в аккаунт(пассажир)")
async def login(account: Account):
    return controller.login(account=account)


@app.get("/passenger/profile/", tags=[Tags._PROFILE_SETTINGS],
        summary="Получение профеля")
async def get_passenger_profile(token: str = Depends(oauth2_scheme)):
    return controller.get_user_profile(token=token)


@app.post("/passenger/change/profile/", tags=[Tags._PROFILE_SETTINGS],
        summary="Изменение профеля")
async def change_passenger_profile(passenger: Passenger, token: str = Depends(oauth2_scheme)):
    return controller.change_user_profile(user=passenger, token=token)


@app.delete("/passenger/delete/profile/", tags=[Tags._PROFILE_SETTINGS],
        summary="Удаление профеля")
async def delete_profile(token: str = Depends(oauth2_scheme)):
    return controller.delete_profile(token=token)


if __name__ == '__main__':
    uvicorn.run('passenger_register:app', host=os.getenv("HOST", "127.0.0.1"), port=int(os.getenv("PORT", "8002")))
