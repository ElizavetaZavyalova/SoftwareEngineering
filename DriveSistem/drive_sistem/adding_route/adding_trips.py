import uvicorn
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from drive_sistem.adding_route.controller.driver_controller import DriverController
from drive_sistem.adding_route.controller.trips_controller import AddingTripsController
from entity.account import Account
from entity.trip_description import TripDescription

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
drivers = DriverController()
routes = AddingTripsController()

######################Вход###############################
@app.post("/token", tags=[DriverController._LOG_IN])
def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return drivers.login(Account(email=form_data.username, password=form_data.password))


##########################################################
@app.post("/driver/trip/create", tags=[''])
def create_trip(trip_info: TripDescription, token: str = Depends(oauth2_scheme)):
    return routes.create_trip(trip_info=trip_info, token=token)


@app.get("/driver/trips/", tags=[''])
def get_all_trips(token: str = Depends(oauth2_scheme)):
    return routes.get_all_trips(token=token)


@app.get("/driver/trip/{id}/", tags=[''])
def get_trip(id: int, token: str = Depends(oauth2_scheme)):
    return routes.get_trip(id=id, token=token)


@app.patch("/driver/trip/{id}/info", tags=[''])
def update_trip_info(id: int, trip_info: TripDescription, token: str = Depends(oauth2_scheme)):
    return routes.update_trip_info(id=id, trip_info=trip_info, token=token)


@app.delete("/driver/trip/{id}", tags=[''])
def delete_trip(id: int, token: str = Depends(oauth2_scheme)):
    return routes.delete_trip(id=id, token=token)


if __name__ == '__main__':
    uvicorn.run('adding_trips:app', reload=True)
