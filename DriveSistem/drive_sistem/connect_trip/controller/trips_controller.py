from fastapi import HTTPException

from drive_sistem.connect_trip.repository.adding_trips_repository import AddingTripsRepository
from drive_sistem.connect_trip.repository.passenger_repository import PassengerRepository
from tocken_generator.cryptography import Cryptography


class ConnectTripsController:
    _CONNECTING_TRIPS = "Подключение к поездке"
    def __init__(self,passenger_repository: PassengerRepository,trips_repository: AddingTripsRepository):
        self.passengers = passenger_repository
        self.trips = trips_repository

    def connect_to_trip(self, id: int, token: str):
        account = Cryptography().decrypt_token(token)
        passenger = self.passengers.get_account(account)
        if passenger:
            return self.trips.connect_to_trip(id=id, passenger=passenger)
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    def cancel_trip(self,id: int, token: str):
        account = Cryptography().decrypt_token(token)
        passenger = self.passengers.get_account(account)
        if passenger:
            return self.trips.cancel_trip(id=id, passenger=passenger)
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    def get_trip(self,id: int, token: str):
        account = Cryptography().decrypt_token(token)
        passenger = self.passengers.get_account(account)
        if passenger:
            return self.trips.get_trip(id=id, passenger=passenger)
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

