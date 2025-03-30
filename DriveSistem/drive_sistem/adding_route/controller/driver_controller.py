from http.client import HTTPException

from drive_sistem.adding_route.repository.driver_repository import DriverRepository
from entity.account import Account
from tocken_generator.cryptography import Cryptography


class DriverController:
    _LOG_IN='Вход'
    def __init__(self):
        self.drivers = DriverRepository()

    def login(self, account: Account):
        if self.drivers.is_driver(account):
            token = Cryptography().generate_token(account=account)
            return token
        raise HTTPException(status_code=400, detail="Incorrect username or password")