from entity.driver import Driver
from entity.trip_description import TripDescription


class AddingTripsRepository:
    def __init__(self):
        self.trips = []

    def create_trip(self, trip_info: TripDescription, driver: Driver):
        pass

    def get_all_trips(self, driver: Driver):
        pass

    def get_trip(self, id: int, driver: Driver):
        pass

    def update_trip_info(self, id: int, trip_info: TripDescription, driver: Driver):
        pass

    def delete_trip(self, id: int, driver: Driver):
        pass