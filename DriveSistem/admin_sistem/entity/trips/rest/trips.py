from typing import List

from pydantic import BaseModel, constr, ConfigDict


class TripDescription(BaseModel):
    title: str
    info: dict
class DriverInfo(BaseModel):
    account_id: int
    first_name: constr(pattern=r"^[A-Za-zА-Яа-яЁё]{2,50}$")
    last_name: constr(pattern=r"^[A-Za-zА-Яа-яЁё]{2,50}$")
    patronymic: constr(pattern=r"^[A-Za-zА-Яа-яЁё]{2,50}$")
    phone_number: constr(pattern=r'^\+?\d{10,15}$')
    requisites: str
    car_number: str
class PassengerInfo(BaseModel):
    account_id: int
    first_name: constr(pattern=r"^[A-Za-zА-Яа-яЁё]{2,50}$")
    last_name: constr(pattern=r"^[A-Za-zА-Яа-яЁё]{2,50}$")
    patronymic: constr(pattern=r"^[A-Za-zА-Яа-яЁё]{2,50}$")
    phone_number: constr(pattern=r'^\+?\d{10,15}$')
    home_address: str

class Trip(BaseModel):
    driver: DriverInfo
    trip: TripDescription
    passengers: List[PassengerInfo]

    model_config = ConfigDict(from_attributes=True)

