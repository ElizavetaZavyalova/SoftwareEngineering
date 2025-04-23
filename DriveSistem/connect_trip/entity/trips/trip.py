from typing import List

from pydantic import BaseModel, ConfigDict

from connect_trip.entity.passenger.rest.passenger import PassengerInfo


class TripDescription(BaseModel):
    title: str
    info: dict

class Trip(BaseModel):
    driver: dict
    trip: TripDescription
    passengers: List[PassengerInfo]

    model_config = ConfigDict(from_attributes=True)


def create_trip_description(trip_info: TripDescription, driver: dict) -> Trip:
    return Trip(
        driver=driver,
        trip=trip_info,
        passengers=[]
    )
