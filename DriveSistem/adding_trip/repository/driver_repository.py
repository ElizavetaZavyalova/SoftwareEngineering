from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker

from libs.entity.account import Account
from libs.entity.driver.db.driver import Driver_DB, create_driver
from libs.entity.driver.rest.driver import Driver

class DriverRepository:
    def __init__(self, url: str):
        self.url = url
        self.engine = create_engine(self.url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def is_driver(self, account: Account) -> bool:
        with self.SessionLocal() as db:
            user = db.query(Driver_DB).filter(Driver_DB.email == account.email).first()
            return user and user.password == account.password
    def get_account(self, account: Account) -> Driver | None:
        with self.SessionLocal() as db:
            user_db = db.query(Driver_DB).filter(Driver_DB.email == account.email).first()
            return create_driver(user_db)