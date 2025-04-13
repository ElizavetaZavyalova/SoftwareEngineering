from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

from libs.entity.passenger.rest.passenger import Passenger

Base = declarative_base()
class Passenger_DB(Base):
    __tablename__ = 'passengers'
    id = Column(Integer, primary_key=True, index=True)
    first_name=Column(String)
    last_name=Column(String)
    patronymic=Column(String)
    phone = Column(String)
    email = Column(String, unique=True)
    password = Column(String,name='pass')
    home_address = Column(String)


def create_model(model: Passenger) -> Passenger_DB:
    if model is None:
        return None
    return Passenger_DB(first_name=model.first_name,
                        last_name=model.last_name,
                        patronymic=model.patronymic,
                        phone=model.phone_number,
                        email=model.email,
                        password=model.password,
                        home_address=model.home_address)

def update_model(model: Passenger_DB, user: Passenger) -> bool:
        model.first_name = user.first_name
        model.last_name = user.last_name
        model.patronymic = user.patronymic
        model.phone = user.phone_number
        model.email = user.email
        model.home_address = user.home_address
        model.password = user.password
        return model

def create_passenger(model: Passenger_DB) -> Passenger:
    if model is None:
        return None
    return Passenger(first_name=model.first_name,
                        last_name=model.last_name,
                        patronymic=model.patronymic,
                        phone_number=model.phone,
                        email=model.email,
                        password=model.password,
                        home_address=model.home_address)