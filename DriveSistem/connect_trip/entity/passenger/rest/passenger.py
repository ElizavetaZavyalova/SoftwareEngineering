from pydantic import BaseModel, constr

from connect_trip.entity.passenger.db.user import User


class Passenger(User):
    home_address: str

    class Config:
        orm_mode = True

class PassengerInfo(BaseModel):
    account_id: int
    first_name: constr(pattern=r"^[A-Za-zА-Яа-яЁё]{2,50}$")
    last_name: constr(pattern=r"^[A-Za-zА-Яа-яЁё]{2,50}$")
    patronymic: constr(pattern=r"^[A-Za-zА-Яа-яЁё]{2,50}$")
    phone_number: constr(pattern=r'^\+?\d{10,15}$')
    home_address: str
