from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from admin_sistem.entity.passenger.db.passenger import Passenger_DB, create_passenger, update_model
from admin_sistem.entity.passenger.rest.passenger import Passenger


class PassengerRepository:
    def __init__(self, url: str):
        self.url = url
        self.engine = create_engine(self.url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_passengers(self) -> list:
        with self.SessionLocal() as db:
            return [(passenger.id, create_passenger(passenger)) for passenger in db.query(Passenger_DB).all()]

    def delete_passenger(self, id: int):
        with self.SessionLocal() as db:
            user = db.query(Passenger_DB).filter(Passenger_DB.id == id).first()
            if user:
                db.delete(user)
                db.commit()

    def get_passenger(self, id: int) -> Passenger:
        with self.SessionLocal() as db:
            passenger = db.query(Passenger_DB).filter(Passenger_DB.id == id).first()
            if passenger:
                return create_passenger(passenger)

    def change_passenger(self, id: int, passenger: Passenger):
        with self.SessionLocal() as db:
            passenger_db = db.query(Passenger_DB).filter(Passenger_DB.id == id).first()
            if passenger:
                update_model(passenger_db, passenger)
                db.commit()
