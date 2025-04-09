from fastapi import HTTPException

from admin_sistem.repository.admin_repository import AdminRepository
from admin_sistem.repository.passenger_repository import PassengerRepository
from tocken_generator.cryptography import Cryptography


class PassengerController:
    _PASSENGERS = 'Пассажиры'
    def __init__(self, passengers:PassengerRepository, admin_repository:AdminRepository):
        self.passengers = passengers
        self.admins = admin_repository

    def get_passengers(self, token:str) -> list:
        account = Cryptography().decrypt_token(token)
        if self.admins.is_admin(account):
            return self.passengers.get_passengers()
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    def delete_passenger(self, token:str, id: int):
        account = Cryptography().decrypt_token(token)
        if self.admins.is_admin(account):
            return self.passengers.delete_passenger(id)
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    def get_passenger(self, token:str, id: int):
        account = Cryptography().decrypt_token(token)
        if self.admins.is_admin(account):
            return self.passengers.get_passenger(id)
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    def change_passenger(self,id:int, token:str, passenger):
        account = Cryptography().decrypt_token(token)
        if self.admins.is_admin(account):
            return self.passengers.change_passenger(id=id,passenger=passenger)
        raise HTTPException(status_code=400, detail="Incorrect username or password")

