import os

import uvicorn
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

from account_sistem.driver.driver_repository.redis import DriverRepositoryRedis
from account_sistem.controller.controller import Controller, Tags
from entity.account import Account
from account_sistem.entity.email_confirmation import EmailConfirmation

from account_sistem.driver.driver_repository.rdbms import DriverRepositoryRDBMS
from entity.driver.rest.driver import Driver

app = FastAPI(
    title="FastAPI Token Authentication",
    description="API для ригестрации водителя",
    version="1.0",
    docs_url="/docs"
)
redis_repository = DriverRepositoryRedis()
account_repository = DriverRepositoryRDBMS(
    os.getenv("DATABASE_DRIVER_URL", "postgresql://root:root@localhost:5501/drivers"))
controller = Controller(redis=redis_repository, rdbms=account_repository)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.post("/token", tags=[Tags._LOG_IN], summary="Получение токена")
def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return controller.login(Account(email=form_data.username, password=form_data.password))


# # # # # #
@app.post('/driver/register/', tags=[Tags._REGISTER], summary="Регистрация водителя")
def register_driver(driver: Driver):
    return controller.register_user(user=driver)


@app.post('/driver/confirm/email/', tags=[Tags._REGISTER], summary="Подтверждения email")
def confirm_email_driver(email_confirmation: EmailConfirmation):
    return controller.confirm_email(email_confirmation=email_confirmation)


@app.post('/driver/forgot/password/', tags=[Tags._PASSWORD_RECOVERY], summary="Востановление пароля")
def forgot_password(account: Account):
    return controller.forgot_password(account=account)


@app.post('/driver/change/password/', tags=[Tags._PASSWORD_RECOVERY], summary="Подтверждения нового пароля")
def change_password(email_confirmation: EmailConfirmation):
    return controller.change_password(email_confirmation=email_confirmation)


@app.post("/driver/login", tags=[Tags._LOG_IN], summary="Вход в аккаунт(водитель)")
def login(account: Account):
    return controller.login(account=account)


@app.get("/driver/profile/", tags=[Tags._PROFILE_SETTINGS], summary="Получение профеля")
def get_driver_profile(token: str = Depends(oauth2_scheme)):
    return controller.get_user_profile(token=token)


@app.post("/driver/change/profile/", tags=[Tags._PROFILE_SETTINGS], summary="Изменение профеля")
def change_driver_profile(driver: Driver, token: str = Depends(oauth2_scheme)):
    return controller.change_user_profile(user=driver, token=token)


@app.delete("/driver/delete/profile/", tags=[Tags._PROFILE_SETTINGS], summary="Удаление профеля")
def delete_profile(token: str = Depends(oauth2_scheme)):
    return controller.delete_profile(token=token)


if __name__ == '__main__':
    uvicorn.run('driver_register:app', host=os.getenv("HOST", "127.0.0.1"), port=int(os.getenv("PORT", "8003")))
