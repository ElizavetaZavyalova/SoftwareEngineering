from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from account_sistem.repository.repositoryrdbms import RepositoryRDBMS
from entity.account import Account
from entity.driver.db.driver import Driver_DB, create_driver, create_model, update_model
from entity.driver.rest.driver import Driver


class DriverRepositoryRDBMS(RepositoryRDBMS):
    def __init__(self, url: str):
        self.url = url
        self.engine = create_engine(self.url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def register_user(self, user: Driver) -> None:
        # Если нет user c email то добавить иначе ошибка(((((((((((((((((((((
        return self._add_user(user)

    def _add_user(self, user: Driver) -> None:
        if self.find_user(user.email):
            raise HTTPException(status_code=400, detail=f"Пользователь с email {user.email} уже зарегистрирован.")
        db_user = create_model(user)
        with self.SessionLocal() as db:
            db.add(db_user)
            db.commit()
            db.refresh(db_user)

    def find_user(self, email: str) -> bool:
        # Существует ли user c email(((((((((((((((((((((((
        with self.SessionLocal() as db:
            user = db.query(Driver_DB).filter(Driver_DB.email == email).first()
            return user is not None

    def update_profile(self, account: Account, user: Driver) -> bool:
        if account.email == user.email:
            return self._update_profile(account, user)
        if self.find_user(user.email):
            return False
        return self._update_profile(account, user)
    def _update_profile(self, account: Account, user: Driver):
        with self.SessionLocal() as db:
            user_db = db.query(Driver_DB).filter(Driver_DB.email == account.email).first()
            if not user:
                return False
            update_model(user_db, user)
            db.commit()
            return True

    def _delete_user_by_email(self, email: str) -> bool:
        # удалить пользователя если он существует((((((((((((((((((((((((
        with self.SessionLocal() as db:
            user = db.query(Driver_DB).filter(Driver_DB.email == email).first()
            if not user:
                return False
            db.delete(user)
            db.commit()
            return True

    def delete_profile(self, account: Account, ) -> bool:
        # удалить пользователя если он существует((((((((((((((((((((((((
        return self._delete_user_by_email(account.email)

    def get_user_by_email(self, email: str) -> Driver:
        # Получить user c по email (((((((((((((((((((((((((
        with self.SessionLocal() as db:
            user_db = db.query(Driver_DB).filter(Driver_DB.email == email).first()
            return create_driver(user_db)

    def get_account(self, account: Account) -> Driver | None:
        # Получить user c по еmail ((((((((((((((((((((((((
        with self.SessionLocal() as db:
            user_db = db.query(Driver_DB).filter(Driver_DB.email == account.email).first()
            return create_driver(user_db)

    def change_password(self, account: Account) -> bool:
        # Обновить пароль по еmail((((((((((((((((((((((((
        with self.SessionLocal() as db:
            user = db.query(Driver_DB).filter(Driver_DB.email == account.email).first()
            if not user:
                return False
            user.password = account.password
            db.commit()
            return True

    def find_account(self, account: Account) -> bool:
        # Проверить существование пользователя email password(((((((((((((((((((
        with self.SessionLocal() as db:
            user = db.query(Driver_DB).filter(Driver_DB.email == account.email).first()
            return user and user.password == account.password