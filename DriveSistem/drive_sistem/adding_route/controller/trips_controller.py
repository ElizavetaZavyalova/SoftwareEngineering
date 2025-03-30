from fastapi import HTTPException

from drive_sistem.adding_route.repository.adding_trips_repository import AddingTripsRepository
from drive_sistem.adding_route.repository.driver_repository import DriverRepository
from entity.trip_description import TripDescription
from tocken_generator.cryptography import Cryptography


class AddingTripsController:
    _EDITING_TRIPS="Редактирование поездок"
    def __init__(self):
        self.drivers = DriverRepository()
        self.routes = AddingTripsRepository()

    def create_trip(self, trip_info: TripDescription, token: str):
        account = Cryptography().decrypt_token(token)
        driver = self.drivers.get_account(account)
        if driver:
            return self.routes.create_trip(trip_info=trip_info, driver=driver)
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    def get_all_trips(self, token: str):
        account = Cryptography().decrypt_token(token)
        driver = self.drivers.get_account(account)
        if driver:
            return self.routes.get_all_trips(driver=driver)
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    def get_trip(self, id: int, token: str):
        account = Cryptography().decrypt_token(token)
        driver = self.drivers.get_account(account)
        if driver:
            return self.routes.get_trip(id=id, driver=driver)
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    def update_trip_info(self, id: int, trip_info: TripDescription, token: str):
        account = Cryptography().decrypt_token(token)
        driver = self.drivers.get_account(account)
        if driver:
            return self.routes.update_trip_info(id=id, trip_info=trip_info, driver=driver)
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    def delete_trip(self, id: int, token: str):
        account = Cryptography().decrypt_token(token)
        driver = self.drivers.get_account(account)
        if driver:
            return self.routes.delete_trip(id=id, driver=driver)
        raise HTTPException(status_code=400, detail="Incorrect username or password")
