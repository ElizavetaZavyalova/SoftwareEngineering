from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker

from adding_trip.entity.driver.db.driver import Driver_DB, create_driver_info

from adding_trip.entity.driver.rest.driver import DriverInfo
from libs.tocken_generator.entity.account import Account
class DriverRepository:
    def __init__(self, url: str):
        self.url = url
        self.engine = create_engine(self.url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def is_driver(self, account: Account) -> bool:
        with self.SessionLocal() as db:
            user = db.query(Driver_DB).filter(Driver_DB.email == account.email).first()
            return user and user.password == account.password
    def get_account(self, account: Account) -> DriverInfo | None:
        with self.SessionLocal() as db:
            user_db = db.query(Driver_DB).filter(Driver_DB.email == account.email).first()
            return create_driver_info(user_db)