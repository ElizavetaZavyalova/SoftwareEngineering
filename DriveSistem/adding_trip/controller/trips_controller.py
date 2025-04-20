from fastapi import HTTPException
from starlette.responses import JSONResponse

from adding_trip.entity.trips.trip import TripDescription
from adding_trip.repository.adding_trips_repository import AddingTripsRepository
from adding_trip.repository.driver_repository import DriverRepository
from libs.tocken_generator.cryptography import Cryptography


class AddingTripsController:
    _EDITING_TRIPS = "Редактирование поездок"

    def __init__(self, driver_repository: DriverRepository, trips_repository: AddingTripsRepository):
        self.drivers = driver_repository
        self.trips = trips_repository

    def create_trip(self, trip_info: TripDescription, token: str):
        account = Cryptography().decrypt_token(token)
        driver = self.drivers.get_account(account)
        if driver:
            result = self.trips.create_trip(trip_info=trip_info, driver=driver)
            return JSONResponse(status_code=200,
                                content={"status": "ok", "insert_id": str(result)})
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    def get_all_trips(self, token: str):
        account = Cryptography().decrypt_token(token)
        driver = self.drivers.get_account(account)
        if driver:
            trips = self.trips.get_all_trips(driver=driver)
            if not trips:
                raise HTTPException(status_code=404, detail="No trips found for this driver")
            return JSONResponse(status_code=200,
                                content={"trips": trips})
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    def get_trip(self, id: str, token: str):
        account = Cryptography().decrypt_token(token)
        driver = self.drivers.get_account(account)
        if driver:
            trip = self.trips.get_trip(id=id, driver=driver)
            return JSONResponse(status_code=200,
                                content={"trips": trip.model_dump(exclude_none=True, by_alias=True)})
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    def update_trip_info(self, id: str, trip_info: TripDescription, token: str):
        account = Cryptography().decrypt_token(token)
        driver = self.drivers.get_account(account)
        if driver:
            return JSONResponse(status_code=200,
                                content={"status": "ok",
                                        "count_update": self.trips.update_trip_info(id=id,
                                        trip_info=trip_info, driver=driver)})
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    def delete_trip(self, id: str, token: str):
        account = Cryptography().decrypt_token(token)
        driver = self.drivers.get_account(account)
        if driver:
            count_delete = self.trips.delete_trip(id=id, driver=driver)
            return JSONResponse(status_code=200,
                                content={"status": "ok", "count_delete": str(count_delete)})
        raise HTTPException(status_code=400, detail="Incorrect username or password")
