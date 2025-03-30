from drive_sistem.adding_route.adding_route import create_trip
from entity.driver import Driver
from entity.passenger import Passenger
from entity.trip_description import TripDescription


class AddingRouteRepository:
    def __init__(self):
        self.trips = []

    def connect_to_trip(self,id: int, passenger: Passenger):
        pass

    def cancel_trip(self,id: int,  passenger: Passenger):
        pass

    def get_trip(self,id: int,  passenger: Passenger):
        pass

    def get_trips(self, passenger: Passenger):
        pass

    def get_connected_trips(self, passenger: Passenger):
        pass