from http.client import HTTPException

from drive_sistem.connect_route.repository.passenger_repository import PassengerRepository
from entity.account import Account
from tocken_generator.cryptography import Cryptography


class PassengerController:
    _LOG_IN='Вход'
    def __init__(self):
        self.passengers = PassengerRepository()

    def login(self, account: Account):
        if self.passengers.is_passenger(account):
            token = Cryptography().generate_token(account=account)
            return token
        raise HTTPException(status_code=400, detail="Incorrect username or password")