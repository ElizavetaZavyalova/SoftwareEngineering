from tokenize import String

from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

from entity.passenger import Passenger

Base = declarative_base()
class Passenger_DB(Base):
    __tablename__ = 'passengers_table'
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

class PassengerRepository:
    def __init__(self, url: str):
        self.url = url
        self.engine = create_engine(self.url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def update_model(self, model: Passenger_DB, user: Passenger) -> bool:
        model.first_name = user.first_name
        model.last_name = user.last_name
        model.patronymic = user.patronymic
        model.phone = user.phone_number
        model.email = user.email
        model.car_number = user.car_number
        model.requisites = user.requisites
        model.password = user.password
        return model

    def get_passengers(self) -> list:
        with self.SessionLocal() as db:
            passengers = db.query(Passenger_DB).all()
            return list(map(create_passenger, passengers))

    def delete_passenger(self, id: int):
        with self.SessionLocal() as db:
            user = db.query(Passenger_DB).filter(Passenger_DB.id == id).first()
            if user:
                db.delete(user)
                db.commit()
    def get_passenger(self, id: int)->Passenger:
        with self.SessionLocal() as db:
            passenger=db.query(Passenger_DB).filter(Passenger_DB.id == id).first()
            if passenger:
                return create_passenger(passenger)

    def change_passenger(self, passenger:Passenger):
        with self.SessionLocal() as db:
            passenger_db = db.query(Passenger_DB).filter(Passenger_DB.id == id).first()
            if passenger:
                self.update_model(passenger_db, passenger)
                db.commit()