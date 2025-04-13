import os

import uvicorn
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from starlette.responses import JSONResponse

from admin_sistem.repository.trips_repository import TripsRepository
from drive_sistem.adding_trip.controller.driver_controller import DriverController
from drive_sistem.adding_trip.controller.trips_controller import AddingTripsController
from drive_sistem.adding_trip.repository.driver_repository import DriverRepository
from entity.account import Account
from entity.trip.trip_description import TripDescription

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

driver_repository = DriverRepository(
    url=os.getenv("DATABASE_DRIVER_URL", "postgresql://root:root@localhost:5501/drivers"))
trips_repository = TripsRepository()
drivers = DriverController(driver_repository=driver_repository)
routes = AddingTripsController(driver_repository=driver_repository, trips_repository=trips_repository)

@app.get("/health", tags=["Health"])
def healthcheck():
    return JSONResponse(content={"status": "ok"})


######################Вход###############################
@app.post("/token", tags=[DriverController._LOG_IN], summary="Получение токена")
def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return drivers.login(Account(email=form_data.username, password=form_data.password))


##########################################################
@app.post("/driver/trip/create", tags=[AddingTripsController._EDITING_TRIPS],
        summary="Создание поездки с текущим водителем")
def create_trip(trip_info: TripDescription, token: str = Depends(oauth2_scheme)):
    return routes.create_trip(trip_info=trip_info, token=token)


@app.get("/driver/trips/", tags=[AddingTripsController._EDITING_TRIPS],
        summary="Получение всех поездок текущего водителя")
def get_all_trips(token: str = Depends(oauth2_scheme)):
    return routes.get_all_trips(token=token)


@app.get("/driver/trip/{id}/", tags=[AddingTripsController._EDITING_TRIPS],
        summary="Получение конкретной поездки по id")
def get_trip(id: int, token: str = Depends(oauth2_scheme)):
    return routes.get_trip(id=id, token=token)


@app.patch("/driver/trip/{id}/info", tags=[AddingTripsController._EDITING_TRIPS],
        summary="Обновление информации о поездке по id")
def update_trip_info(id: int, trip_info: TripDescription, token: str = Depends(oauth2_scheme)):
    return routes.update_trip_info(id=id, trip_info=trip_info, token=token)


@app.delete("/driver/trip/{id}", tags=[AddingTripsController._EDITING_TRIPS], summary="Удаление поездки по id")
def delete_trip(id: int, token: str = Depends(oauth2_scheme)):
    return routes.delete_trip(id=id, token=token)


if __name__ == '__main__':
    uvicorn.run('adding_trips:app', host=os.getenv("HOST", "127.0.0.1"), port=int(os.getenv("PORT", "8004")))
