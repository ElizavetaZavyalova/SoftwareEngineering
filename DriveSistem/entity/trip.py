from pydantic import BaseModel

from entity.driver import Driver
from entity.passenger import Passenger
from entity.trip_description import TripDescription


class Trip(BaseModel):
    trip_id: int
    trip_info: TripDescription
    passengers: list[Passenger]
    driver: Driver