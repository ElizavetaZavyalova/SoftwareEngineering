from http.client import HTTPException

from drive_sistem.adding_trip.repository.driver_repository import DriverRepository
from entity.account import Account
from tocken_generator.cryptography import Cryptography


class DriverController:
    _LOG_IN='Вход'
    def __init__(self, driver_repository: DriverRepository):
        self.drivers = driver_repository

    def login(self, account: Account):
        if self.drivers.is_driver(account):
            token = Cryptography().generate_token(account=account)
            return token
        raise HTTPException(status_code=400, detail="Incorrect username or password")