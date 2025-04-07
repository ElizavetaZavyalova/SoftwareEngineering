from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from entity.driver import Driver

Base = declarative_base()
class Driver_DB(Base):
    __tablename__ = 'drivers_table'
    id = Column(Integer, primary_key=True, index=True)
    first_name=Column(String)
    last_name=Column(String)
    patronymic=Column(String)
    phone = Column(String)
    email = Column(String, unique=True)
    password = Column(String,name='pass')
    requisites= Column(String)
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


def create_driver(model: Driver_DB) -> Driver:
    if model is None:
        return None
    return Driver(first_name=model.first_name,
                        last_name=model.last_name,
                        patronymic=model.patronymic,
                        phone_number=model.phone,
                        email=model.email,
                        password=model.password,
                        requisites = model.requisites,
                        car_number = model.car_number)

class DriverRepository:
    def __init__(self, url: str):
        self.url = url
        self.engine = create_engine(self.url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def update_model(self, model: Driver_DB, user: Driver) -> bool:
        model.first_name = user.first_name
        model.last_name = user.last_name
        model.patronymic = user.patronymic
        model.phone = user.phone_number
        model.email = user.email
        model.car_number = user.car_number
        model.requisites = user.requisites
        model.password = user.password
        return model

    def get_drivers(self) -> list:
        with self.SessionLocal() as db:
            drivers = db.query(Driver_DB).all()
            return list(map(create_driver, drivers))

    def delete_driver(self, id: int):
        with self.SessionLocal() as db:
            user = db.query(Driver_DB).filter(Driver_DB.id == id).first()
            if user:
                db.delete(user)
                db.commit()
    def get_driver(self, id: int)->Driver:
        with self.SessionLocal() as db:
            driver=db.query(Driver_DB).filter(Driver_DB.id == id).first()
            if driver:
                return create_driver(driver)

    def change_driver(self, driver:Driver):
        with self.SessionLocal() as db:
            driver_db = db.query(Driver_DB).filter(Driver_DB.id == id).first()
            if driver:
                self.update_model(driver_db, driver)
                db.commit()