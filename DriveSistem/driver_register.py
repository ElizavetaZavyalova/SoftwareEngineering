import os

import uvicorn
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from starlette.responses import JSONResponse

from driver.account_sistem.controller.controller import Controller, Tags
from driver.driver.rest.driver import Driver
from driver.driver_repository.redis import DriverRepositoryRedis
from libs.tocken_generator.entity.account import Account

from driver.driver_repository.rdbms import DriverRepositoryRDBMS

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


@app.get("/health", tags=["Health"])
async def healthcheck():
    return JSONResponse(content={"status": "ok"})


@app.post("/token", tags=[Tags._LOG_IN],
        summary="Получение токена")
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return controller.login(Account(email=form_data.username, password=form_data.password))


# # # # # #
@app.post('/driver/register/', tags=[Tags._REGISTER],
        summary="Регистрация водителя")
async def register_driver(driver: Driver):
    return controller.register_user(user=driver)


@app.post('/driver/confirm/email/', tags=[Tags._REGISTER],
        summary="Подтверждения email")
async def confirm_email_driver(email_confirmation: EmailConfirmation):
    return controller.confirm_email(email_confirmation=email_confirmation)


@app.post('/driver/forgot/password/', tags=[Tags._PASSWORD_RECOVERY],
        summary="Востановление пароля")
async def forgot_password(account: Account):
    return controller.forgot_password(account=account)


@app.post('/driver/change/password/', tags=[Tags._PASSWORD_RECOVERY],
        summary="Подтверждения нового пароля")
async def change_password(email_confirmation: EmailConfirmation):
    return controller.change_password(email_confirmation=email_confirmation)


@app.post("/driver/login", tags=[Tags._LOG_IN],
        summary="Вход в аккаунт(водитель)")
async def login(account: Account):
    return controller.login(account=account)


@app.get("/driver/profile/", tags=[Tags._PROFILE_SETTINGS],
        summary="Получение профеля")
async def get_driver_profile(token: str = Depends(oauth2_scheme)):
    return controller.get_user_profile(token=token)


@app.post("/driver/change/profile/", tags=[Tags._PROFILE_SETTINGS],
        summary="Изменение профеля")
async def change_driver_profile(driver: Driver, token: str = Depends(oauth2_scheme)):
    return controller.change_user_profile(user=driver, token=token)


@app.delete("/driver/delete/profile/", tags=[Tags._PROFILE_SETTINGS],
        summary="Удаление профеля")
async def delete_profile(token: str = Depends(oauth2_scheme)):
    return controller.delete_profile(token=token)


if __name__ == '__main__':
    uvicorn.run('driver_register:app', host=os.getenv("HOST", "127.0.0.1"), port=int(os.getenv("PORT", "8003")))
