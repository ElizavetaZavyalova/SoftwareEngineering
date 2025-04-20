from pydantic import BaseModel




class TripDescription(BaseModel):
    title: str
    info: dict


class Trip(BaseModel):
    driver: {}
    trip: TripDescription
    passengers: list


def create_trip_description(trip_info: TripDescription, driver: {}) -> Trip:
    return Trip(
        driver=driver,
        trip=trip_info,
        passengers=[]
    )
