from fastapi import HTTPException

from admin_sistem.repository.admin_repository import AdminRepository
from admin_sistem.repository.driver_repository import DriverRepository
from tocken_generator.cryptography import Cryptography

class DriverController:
    _DRIVERS='Водители'
    def __init__(self, drivers: DriverRepository, admin_repository: AdminRepository):
        self.drivers = drivers
        self.admins = admin_repository

    def get_drivers(self, token:str) -> list:
        account = Cryptography().decrypt_token(token)
        if self.admins.is_admin(account):
            return self.drivers.get_drivers()
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    def delete_driver(self, token:str, id: int):
        account = Cryptography().decrypt_token(token)
        if self.admins.is_admin(account):
            return self.drivers.delete_driver(id)
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    def get_driver(self, token:str, id: int):
        account = Cryptography().decrypt_token(token)
        if self.admins.is_admin(account):
            return self.drivers.get_driver(id)
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    def change_driver(self,id:int, token:str, driver):
        account = Cryptography().decrypt_token(token)
        if self.admins.is_admin(account):
            return self.drivers.change_driver(driver)
        raise HTTPException(status_code=400, detail="Incorrect username or password")

