from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

from account_sistem.repository.repositoryrdbms import RepositoryRDBMS
from entity.account import Account
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


class PassengerRepositoryRDBMS(RepositoryRDBMS):
    def __init__(self, url: str):
        self.url = url
        self.engine = create_engine(self.url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def register_user(self, user: Passenger) -> None:
        # Если нет user c email то добавить иначе ошибка(((((((((((((((((((((
        self._add_user(user)

    def _add_user(self, user: Passenger) -> None:
        if self.find_user(user.email):
            raise ValueError(f"Пользователь с email {user.email} уже зарегистрирован.")
        db_user = create_model(user)
        with self.SessionLocal() as db:
            db.add(db_user)
            db.commit()
            db.refresh(db_user)

    def find_user(self, email: str) -> bool:
        # Существует ли user c email(((((((((((((((((((((((
        with self.SessionLocal() as db:
            user = db.query(Passenger_DB).filter(Passenger_DB.email == email).first()
            return user is not None

    def update_profile(self, account: Account, user: Passenger) -> bool:
        if account.email == user.email:
            with self.SessionLocal() as db:
                user_db = db.query(Passenger_DB).filter(Passenger_DB.email == account.email).first()
                if not user:
                    return False
                self.update_model(user_db, user)
                db.commit()
                return True
        if self.find_user(user.email):
            return False
        self._delete_user_by_email(account.email)
        self._add_user(user)
        return True

    def update_model(self, model: Passenger_DB, user: Passenger) -> bool:
        model.first_name = user.first_name
        model.last_name = user.last_name
        model.patronymic = user.patronymic
        model.phone = user.phone_number
        model.email = user.email
        model.home_address = user.home_address
        model.password = user.password
        return model

    def _delete_user_by_email(self, email: str) -> bool:
        # удалить пользователя если он существует((((((((((((((((((((((((
        with self.SessionLocal() as db:
            user = db.query(Passenger_DB).filter(Passenger_DB.email == email).first()
            if not user:
                return False
            db.delete(user)
            db.commit()
            return True

    def delete_profile(self, account: Account, ) -> bool:
        # удалить пользователя если он существует((((((((((((((((((((((((
        return self._delete_user_by_email(account.email)

    def get_user_by_email(self, email: str) -> Passenger:
        # Получить user c по email (((((((((((((((((((((((((
        with self.SessionLocal() as db:
            user_db = db.query(Passenger_DB).filter(Passenger_DB.email == email).first()
            return create_passenger(user_db)

    def get_account(self, account: Account) -> Passenger | None:
        # Получить user c по еmail ((((((((((((((((((((((((
        with self.SessionLocal() as db:
            user_db = db.query(Passenger_DB).filter(Passenger_DB.email == account.email).first()
            return create_passenger(user_db)

    def change_password(self, account: Account) -> bool:
        # Обновить пароль по еmail((((((((((((((((((((((((
        with self.SessionLocal() as db:
            user = db.query(Passenger_DB).filter(Passenger_DB.email == account.email).first()
            if not user:
                return False
            user.password = account.password
            db.commit()
            return True

    def find_account(self, account: Account) -> bool:
        # Проверить существование пользователя email password(((((((((((((((((((
        with self.SessionLocal() as db:
            user = db.query(Passenger_DB).filter(Passenger_DB.email == account.email).first()
            return user and user.password == account.password
