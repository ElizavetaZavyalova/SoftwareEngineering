from pydantic import BaseModel

from libs.entity.driver.rest.driver import Driver
from libs.entity.passenger.rest.passenger import Passenger
from libs.entity.trip.trip_description import TripDescription


class Trip(BaseModel):
    trip_id: int
    trip_info: TripDescription
    passengers: list[Passenger]
    driver: Driver