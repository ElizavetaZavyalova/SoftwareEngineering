import uvicorn
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

from register_sistem.autontification.controller.controller import Controller, Tags
from entity.account import Account
from register_sistem.autontification.entity.email_confirmation import EmailConfirmation
from register_sistem.autontification.repository.redis import Redis
from entity.passenger import Passenger
from register_sistem.autontification.passenger.passenger_repository.rdbms import PassengerRepositoryRDBMS

app = FastAPI(
    title="FastAPI Token Authentication",
    description="API для ригестрации пассажира",
    version="1.0",
    docs_url="/docs"
)
redis_repository = Redis()
account_repository = PassengerRepositoryRDBMS()
controller = Controller(redis_repository, account_repository)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
@app.post("/token",tags=[Tags._LOG_IN])
def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return controller.login(Account(email=form_data.username, password=form_data.password))
# # # # # #
@app.post('/passenger/register/', tags=[Tags._REGISTER])
def register_passenger(passenger: Passenger):
    return controller.register_user(user=passenger)

@app.post('/passenger/confirm/email/', tags=[Tags._REGISTER])
def confirm_email_passenger(email_confirmation: EmailConfirmation):
    return controller.confirm_email_passenger(email_confirmation=email_confirmation)

@app.post('/passenger/forgot/password/', tags=[Tags._PASSWORD_RECOVERY])
def forgot_password(account: Account):
    return controller.forgot_password(account=account)


@app.post('/passenger/change/password/', tags=[Tags._PASSWORD_RECOVERY])
def change_password(email_confirmation: EmailConfirmation):
    return controller.change_password(email_confirmation=email_confirmation)

@app.post("/passenger/login", tags=[Tags._LOG_IN])
def login(account: Account):
    return controller.login(account=account)

@app.get("/passenger/profile/", tags=[Tags._PROFILE_SETTINGS])
def get_passenger_profile(token: str = Depends(oauth2_scheme)):
    return controller.get_user_profile(token=token)

@app.post("/passenger/change/profile/", tags=[Tags._PROFILE_SETTINGS])
def change_passenger_profile(passenger: Passenger, token: str = Depends(oauth2_scheme)):
    return controller.change_user_profile(user=passenger, token=token)

@app.delete("/passenger/delete/profile/", tags=[Tags._PROFILE_SETTINGS])
def delete_profile(token: str = Depends(oauth2_scheme)):
    return controller.delete_profile(token=token)


if __name__ == '__main__':
    uvicorn.run('passenger_register:app', reload=True)
