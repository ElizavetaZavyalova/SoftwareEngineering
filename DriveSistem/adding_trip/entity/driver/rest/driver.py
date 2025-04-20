from pydantic import constr, BaseModel

from adding_trip.entity.driver.rest.user import User


class Driver(User):
    requisites: str
    car_number: str

class DriverInfo(BaseModel):
    account_id: int
    first_name: constr(pattern=r"^[A-Za-zА-Яа-яЁё]{2,50}$")
    last_name: constr(pattern=r"^[A-Za-zА-Яа-яЁё]{2,50}$")
    patronymic: constr(pattern=r"^[A-Za-zА-Яа-яЁё]{2,50}$")
    phone_number: constr(pattern=r'^\+?\d{10,15}$')
    requisites: str
    car_number: str
