from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from libs.entity.driver.db.driver import Driver_DB, create_driver, update_model
from libs.entity.driver.rest.driver import Driver


class DriverRepository:
    def __init__(self, url: str):
        self.url = url
        self.engine = create_engine(self.url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_drivers(self) -> list:
        with self.SessionLocal() as db:
            return [(driver.id, create_driver(driver)) for driver in db.query(Driver_DB).all()]

    def delete_driver(self, id: int):
        with self.SessionLocal() as db:
            user = db.query(Driver_DB).filter(Driver_DB.id == id).first()
            if user:
                db.delete(user)
                db.commit()

    def get_driver(self, id: int) -> Driver:
        with self.SessionLocal() as db:
            driver = db.query(Driver_DB).filter(Driver_DB.id == id).first()
            if driver:
                return create_driver(driver)

    def change_driver(self, id: int, driver: Driver):
        with self.SessionLocal() as db:
            driver_db = db.query(Driver_DB).filter(Driver_DB.id == id).first()
            if driver:
                update_model(driver_db, driver)
                db.commit()
