from pydantic import BaseModel

from entity.driver.rest.driver import Driver
from entity.passenger.rest.passenger import Passenger
from entity.trip.trip_description import TripDescription


class Trip(BaseModel):
    trip_id: int
    trip_info: TripDescription
    passengers: list[Passenger]
    driver: Driver