from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from admin_sistem.entity.admins.db.admin import Admin_DB
from libs.tocken_generator.entity.account import Account



class AdminRepository:
    def __init__(self, url: str):
        self.url = url
        self.engine = create_engine(self.url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def is_admin(self, account: Account) -> bool:
        with self.SessionLocal() as db:
            admin = db.query(Admin_DB).filter(Admin_DB.email == account.email).first()
            return admin and admin.password == account.password
