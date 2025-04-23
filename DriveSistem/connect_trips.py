import os

import uvicorn
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from starlette.responses import JSONResponse

from connect_trip.controller.passenger_controller import PassengerController
from connect_trip.controller.trips_controller import ConnectTripsController
from connect_trip.repository.connect_trips_repository import ConnectTripsRepository
from connect_trip.repository.passenger_repository import PassengerRepository
from libs.tocken_generator.entity.account import Account


app = FastAPI(
    title="FastAPI Token Authentication",
    description="API для подключения к поездке",
    version="1.0",
    docs_url="/docs"
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
passenger_repository = PassengerRepository(
    url=os.getenv("DATABASE_PASSENGER_URL", "postgresql://root:root@localhost:5502/passengers"))
trips_repository = ConnectTripsRepository(url=os.getenv("DATABASE_TRIPS_URL",
                                                    'mongodb://root:root@localhost:27018/'))

passengers = PassengerController(passenger_repository=passenger_repository)
routes = ConnectTripsController(passenger_repository=passenger_repository, trips_repository=trips_repository)


@app.get("/health", tags=["Health"])
async def healthcheck():
    return JSONResponse(content={"status": "ok"})


######################Вход###############################
@app.post("/token", tags=[PassengerController._LOG_IN],
        summary="Получение токена")
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return passengers.login(Account(email=form_data.username, password=form_data.password))


##########################################################
@app.post("/passenger/trip/{id}/connect", tags=[ConnectTripsController._CONNECTING_TRIPS],
        summary="Подключение текущего пассажира к поездке по id")
async def connect_to_trip(id: str, token: str = Depends(oauth2_scheme)):
    return routes.connect_to_trip(id=id, token=token)


@app.delete("/passenger/trip/{id}/cancel", tags=[ConnectTripsController._CONNECTING_TRIPS],
        summary="Отключение текущего пассажира от поездки по id")
async def cancel_trip(id: str, token: str = Depends(oauth2_scheme)):
    return routes.cancel_trip(id=id, token=token)


@app.get("/passenger/trip/{id}/", tags=[ConnectTripsController._CONNECTING_TRIPS],
        summary="Получение поездки по id")
async def get_connected_trip(id: str, token: str = Depends(oauth2_scheme)):
    return routes.get_connected_trip(id=id, token=token)


@app.get("/passenger/trips/{title}", tags=[ConnectTripsController._CONNECTING_TRIPS],
        summary="Получение всех поездок")
async def get_trips(title:str, token: str = Depends(oauth2_scheme)):
    return routes.get_trips(title=title,token=token)


@app.get("/passenger/trips/connected", tags=[ConnectTripsController._CONNECTING_TRIPS],
        summary="Получение всех подключеных поездок")
async def get_connected_trips(token: str = Depends(oauth2_scheme)):
    return routes.get_connected_trips(token=token)


if __name__ == '__main__':
    uvicorn.run('connect_trips:app', host=os.getenv("HOST", "127.0.0.1"), port=int(os.getenv("PORT", "8005")))
