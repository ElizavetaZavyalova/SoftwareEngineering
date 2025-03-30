import uvicorn
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from drive_sistem.route_founder.controller.passenger_controller import PassengerController
from drive_sistem.route_founder.controller.route_controller import RouteController
from entity.account import Account

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
passengers = PassengerController()
routes = RouteController()

######################Вход###############################
@app.post("/token", tags=[''])
def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return passengers.login(Account(email=form_data.username, password=form_data.password))

##########################################################
@app.post("/passenger/trip/{id}/connect", tags=[''])
def connect_to_trip(id:int, token: str = Depends(oauth2_scheme)):
    return routes.connect_to_trip(id=id, token=token)

@app.delete("/passenger/trip/{id}/cancel", tags=[''])
def cancel_trip(id:int, token: str = Depends(oauth2_scheme)):
    return routes.cancel_trip(id=id, token=token)

@app.get("/passenger/trip/{id}/", tags=[''])
def get_trip(id:int, token: str = Depends(oauth2_scheme)):
    return routes.get_trip(id=id, token=token)
@app.get("/passenger/trips/", tags=[''])
def get_trips(token: str = Depends(oauth2_scheme)):
    return routes.get_trips(token=token)
@app.get("/passenger/trips/connected", tags=[''])
def get_connected_trips(token: str = Depends(oauth2_scheme)):
    return routes.get_connected_trips(token=token)

if __name__ == '__main__':
    uvicorn.run('route_founder:app', reload=True)