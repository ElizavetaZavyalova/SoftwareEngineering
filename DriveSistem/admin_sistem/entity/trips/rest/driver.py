from pydantic import BaseModel


class Trip(BaseModel):
    requisites: str
    car_number: str
