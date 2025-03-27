from pydantic import BaseModel


class UserContacts(BaseModel):
    name: str
    email: str
    password: str
    role: str


class User(UserContacts):
    id: int
