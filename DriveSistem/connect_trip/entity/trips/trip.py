from pydantic import BaseModel

from adding_trip.entity.driver.rest.driver import DriverInfo


class TripDescription(BaseModel):
    title: str
    info: dict


class Trip(BaseModel):
    driver: DriverInfo
    trip: TripDescription
    passengers: list


def create_trip_description(trip_info: TripDescription, driver: DriverInfo) -> Trip:
    return Trip(
        driver=driver,
        trip=trip_info,
        passengers=[]
    )
