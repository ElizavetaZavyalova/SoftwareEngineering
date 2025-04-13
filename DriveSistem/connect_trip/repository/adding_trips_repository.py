from libs.entity.passenger.rest.passenger import Passenger


class AddingTripsRepository:
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