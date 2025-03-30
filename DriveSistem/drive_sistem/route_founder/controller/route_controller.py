from fastapi import HTTPException

from drive_sistem.route_founder.repository.adding_route_repository import AddingRouteRepository
from drive_sistem.route_founder.repository.passenger_repository import PassengerRepository
from tocken_generator.cryptography import Cryptography


class RouteController:
    def __init__(self):
        self.passengers = PassengerRepository()
        self.routes = AddingRouteRepository()

    def connect_to_trip(self, id: int, token: str):
        account = Cryptography().decrypt_token(token)
        passenger = self.passengers.get_account(account)
        if passenger:
            return self.routes.connect_to_trip(id=id, passenger=passenger)
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    def cancel_trip(self,id: int, token: str):
        account = Cryptography().decrypt_token(token)
        passenger = self.passengers.get_account(account)
        if passenger:
            return self.routes.cancel_trip(id=id, passenger=passenger)
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    def get_trip(self,id: int, token: str):
        account = Cryptography().decrypt_token(token)
        passenger = self.passengers.get_account(account)
        if passenger:
            return self.routes.get_trip(id=id, passenger=passenger)
        raise HTTPException(status_code=400, detail="Incorrect username or password")


    def get_trips(self,token: str):
        account = Cryptography().decrypt_token(token)
        passenger = self.passengers.get_account(account)
        if passenger:
            return self.routes.get_trips(passenger=passenger)
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    def get_connected_trips(self,token: str):
        account = Cryptography().decrypt_token(token)
        passenger = self.passengers.get_account(account)
        if passenger:
            return self.routes. get_connected_trips(passenger=passenger)
        raise HTTPException(status_code=400, detail="Incorrect username or password")

