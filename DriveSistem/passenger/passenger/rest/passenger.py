from passenger.passenger.rest.user import User


class Passenger(User):
    home_address: str

    class Config:
        orm_mode = True
