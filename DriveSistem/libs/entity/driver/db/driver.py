from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

from libs.entity.driver.rest.driver import Driver

Base = declarative_base()


class Driver_DB(Base):
    __tablename__ = 'drivers'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    patronymic = Column(String)
    phone = Column(String)
    email = Column(String, unique=True)
    password = Column(String, name='pass')
    requisites = Column(String)
    car_number = Column(String)


def create_model(model: Driver) -> Driver_DB:
    if model is None:
        return None
    return Driver_DB(first_name=model.first_name,
                        last_name=model.last_name,
                        patronymic=model.patronymic,
                        phone=model.phone_number,
                        email=model.email,
                        password=model.password,
                        requisites=model.requisites,
                        car_number=model.car_number)


def update_model(model: Driver_DB, user: Driver) -> bool:
    model.first_name = user.first_name
    model.last_name = user.last_name
    model.patronymic = user.patronymic
    model.phone = user.phone_number
    model.email = user.email
    model.car_number = user.car_number
    model.requisites = user.requisites
    model.password = user.password
    return model


def create_driver(model: Driver_DB) -> Driver:
    if model is None:
        return None
    return Driver(first_name=model.first_name,
                    last_name=model.last_name,
                    patronymic=model.patronymic,
                    phone_number=model.phone,
                    email=model.email,
                    password=model.password,
                    requisites=model.requisites,
                    car_number=model.car_number)
