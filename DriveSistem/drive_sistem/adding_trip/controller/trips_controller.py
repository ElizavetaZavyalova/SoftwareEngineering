from fastapi import HTTPException

from admin_sistem.repository.trips_repository import TripsRepository
from drive_sistem.adding_trip.repository.driver_repository import DriverRepository
from entity.trip.trip_description import TripDescription
from tocken_generator.cryptography import Cryptography


class AddingTripsController:
    _EDITING_TRIPS="Редактирование поездок"
    def __init__(self, driver_repository: DriverRepository, trips_repository: TripsRepository):
        self.drivers = driver_repository
        self.trips = trips_repository

    def create_trip(self, trip_info: TripDescription, token: str):
        account = Cryptography().decrypt_token(token)
        driver = self.drivers.get_account(account)
        if driver:
            return self.trips.create_trip(trip_info=trip_info, driver=driver)
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    def get_all_trips(self, token: str):
        account = Cryptography().decrypt_token(token)
        driver = self.drivers.get_account(account)
        if driver:
            return self.trips.get_all_trips(driver=driver)
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    def get_trip(self, id: int, token: str):
        account = Cryptography().decrypt_token(token)
        driver = self.drivers.get_account(account)
        if driver:
            return self.trips.get_trip(id=id, driver=driver)
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    def update_trip_info(self, id: int, trip_info: TripDescription, token: str):
        account = Cryptography().decrypt_token(token)
        driver = self.drivers.get_account(account)
        if driver:
            return self.trips.update_trip_info(id=id, trip_info=trip_info, driver=driver)
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    def delete_trip(self, id: int, token: str):
        account = Cryptography().decrypt_token(token)
        driver = self.drivers.get_account(account)
        if driver:
            return self.trips.delete_trip(id=id, driver=driver)
        raise HTTPException(status_code=400, detail="Incorrect username or password")
