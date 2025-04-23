from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from connect_trip.entity.passenger.db.passenger import create_passenger_info, Passenger_DB
from connect_trip.entity.passenger.rest.passenger import PassengerInfo
from libs.tocken_generator.entity.account import Account


class PassengerRepository:
    def __init__(self, url: str):
        self.url = url
        self.engine = create_engine(self.url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def is_passenger(self, account: Account) -> bool:
        with self.SessionLocal() as db:
            user = db.query(Passenger_DB).filter(Passenger_DB.email == account.email).first()
            return user and user.password == account.password

    def get_account(self, account: Account) -> PassengerInfo | None:
        with self.SessionLocal() as db:
            user_db = db.query(Passenger_DB).filter(Passenger_DB.email == account.email).first()
            return create_passenger_info(user_db)
