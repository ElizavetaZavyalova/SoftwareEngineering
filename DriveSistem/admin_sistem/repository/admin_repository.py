from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from entity.account import Account

Base = declarative_base()
class Admin_DB(Base):
    __tablename__ = 'admins_table'
    id = Column(Integer, primary_key=True, index=True)
    first_name=Column(String)
    last_name=Column(String)
    patronymic=Column(String)
    phone = Column(String)
    email = Column(String, unique=True)
    password = Column(String,name='pass')
class AdminRepository:
    def __init__(self, url: str):
        self.url = url
        self.engine = create_engine(self.url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def is_admin(self, admin: Account) -> bool:
        with self.SessionLocal() as db:
            admin = db.query(Admin_DB).filter(Admin_DB.email == admin.email).first()
            return admin and admin.password == admin.password
