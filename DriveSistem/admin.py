import os

import uvicorn
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

from admin_sistem.controller.admin_controller import AdminController
from admin_sistem.controller.driver_controller import DriverController
from admin_sistem.controller.passenger_controller import PassengerController
from admin_sistem.controller.trips_controller import TripsController
from admin_sistem.repository.admin_repository import AdminRepository
from admin_sistem.repository.driver_repository import DriverRepository
from admin_sistem.repository.passenger_repository import PassengerRepository
from admin_sistem.repository.trips_repository import TripsRepository
from entity.driver import Driver
from entity.passenger import Passenger
from entity.trip import Trip
from entity.account import Account

app = FastAPI(
    title="FastAPI Token Authentication",
    description="API для ригестрации водителя",
    version="1.0",
    docs_url="/docs"
)
trips_repository = TripsRepository()
passengers_repository = PassengerRepository(url=os.getenv("DATABASE_PASSENGER_URL", "postgresql://root:root@localhost:5502/passsengers"))
admins_repository = AdminRepository(url=os.getenv("DATABASE_ADMINS_URL", "postgresql://root:root@localhost:5503/admins"))
drivers_repository = DriverRepository(url=os.getenv("DATABASE_DRIVER_URL", "postgresql://root:root@localhost:5501/drivers"))

passengers = PassengerController(admin_repository=admins_repository, passengers=passengers_repository)
drivers = DriverController(admin_repository=admins_repository, drivers=drivers_repository)
admin = AdminController(admin_repository=admins_repository)
trips = TripsController(trips=trips_repository, admin_repository=admins_repository)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

######################Вход###############################
@app.post("/token", tags=[AdminController._LOG_IN])
def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return admin.login(Account(email=form_data.username, password=form_data.password))
# # # # # #
@app.post("/admin/login", tags=[AdminController._LOG_IN])
def login(account: Account):
    return admin.login(account=account)

##########################################################

######################Водители############################
@app.get("admin/drivers/", tags=[DriverController._DRIVERS])
def get_drivers(token: str = Depends(oauth2_scheme)) -> list:
    return drivers.get_drivers(token=token)
@app.delete("admin/driver/{id}/", tags=[DriverController._DRIVERS])
def delete_driver(id: int, token: str = Depends(oauth2_scheme)):
    return drivers.delete_driver(id=id, token=token)
@app.get("admin/driver/{id}/", tags=[DriverController._DRIVERS])
def get_driver(id: int, token: str = Depends(oauth2_scheme)):
    return drivers.get_driver(id=id, token=token)
@app.post("admin/driver/{id}/", tags=[DriverController._DRIVERS])
def change_driver(driver: Driver, token: str = Depends(oauth2_scheme)):
    return drivers.change_driver(token=token, driver=driver)

##########################################################

######################Пассажиры############################
@app.get("admin/passengers/", tags=[PassengerController._PASSENGERS])
def get_passengers(token: str = Depends(oauth2_scheme)) -> list:
    return passengers.get_passengers(token=token)
@app.delete("admin/passenger/{id}/", tags=[PassengerController._PASSENGERS])
def delete_passenger(id: int, token: str = Depends(oauth2_scheme)):
    return passengers.delete_passenger(id=id, token=token)
@app.get("admin/passenger/{id}/", tags=[PassengerController._PASSENGERS])
def get_passenger(id: int, token: str = Depends(oauth2_scheme)):
    return passengers.get_passenger(id=id, token=token)
@app.post("admin/passenger/{id}/", tags=[PassengerController._PASSENGERS])
def change_passenger(passenger: Passenger, token: str = Depends(oauth2_scheme)):
    return passengers.change_passenger(token=token, passenger=passenger)

##########################################################

######################Поездки############################
@app.get("admin/trips/", tags=[TripsController._TRIPS])
def get_trips(token: str = Depends(oauth2_scheme)) -> list:
    return trips.get_trips(token=token)
@app.delete("admin/trip/{id}/", tags=[TripsController._TRIPS])
def delete_trip(id: int, token: str = Depends(oauth2_scheme)):
    return trips.delete_trip(id=id, token=token)
@app.get("admin/trip/{id}/", tags=[TripsController._TRIPS])
def get_trip(id: int, token: str = Depends(oauth2_scheme)):
    return trips.get_trip(id=id, token=token)
@app.post("admin/trip/{id}/", tags=[TripsController._TRIPS])
def change_trip(trip: Trip, token: str = Depends(oauth2_scheme)):
    return trips.change_trip(token=token, trip=trip)

##########################################################

if __name__ == '__main__':
    uvicorn.run('admin:app', host="0.0.0.0", port=8000)