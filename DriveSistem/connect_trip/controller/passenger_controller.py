from http.client import HTTPException

from connect_trip.repository.passenger_repository import PassengerRepository
from libs.tocken_generator.entity.account import Account
from libs.tocken_generator.cryptography import Cryptography


class PassengerController:
    _LOG_IN = 'Вход'

    def __init__(self, passenger_repository: PassengerRepository):
        self.passengers = passenger_repository

    def login(self, account: Account):
        account.password = Cryptography().hash_password(password=account.password)
        if self.passengers.is_passenger(account):
            token = Cryptography().generate_token(account=account)
            return token
        raise HTTPException(status_code=400, detail="Incorrect username or password")
