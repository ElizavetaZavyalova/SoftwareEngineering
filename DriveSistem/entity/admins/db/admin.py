from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class Admin_DB(Base):
    __tablename__ = 'admins'
    id = Column(Integer, primary_key=True, index=True)
    first_name=Column(String)
    last_name=Column(String)
    patronymic=Column(String)
    phone = Column(String)
    email = Column(String, unique=True)
    password = Column(String,name='pass')