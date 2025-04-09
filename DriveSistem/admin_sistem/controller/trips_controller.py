from fastapi import HTTPException

from admin_sistem.repository.admin_repository import AdminRepository
from admin_sistem.repository.trips_repository import TripsRepository
from tocken_generator.cryptography import Cryptography


class TripsController:
    _TRIPS = 'Поездки'
    def __init__(self,trips: TripsRepository, admin_repository: AdminRepository):
        self.trips = trips
        self.admins = admin_repository

    def get_trips(self, token:str) -> list:
        account = Cryptography().decrypt_token(token)
        if self.admins.is_admin(account):
            return self.trips.get_trips()
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    def delete_trip(self, token:str, id: int):
        account = Cryptography().decrypt_token(token)
        if self.admins.is_admin(account):
            return self.trips.delete_trip(id)
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    def get_trip(self, token:str, id: int):
        account = Cryptography().decrypt_token(token)
        if self.admins.is_admin(account):
            return self.trips.get_trip(id)
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    def change_trip(self,id:int, token:str, trip):
        account = Cryptography().decrypt_token(token)
        if self.admins.is_admin(account):
            return self.trips.change_trip(id=id,trip=trip)
        raise HTTPException(status_code=400, detail="Incorrect username or password")