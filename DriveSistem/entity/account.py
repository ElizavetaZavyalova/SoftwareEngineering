from pydantic import BaseModel, EmailStr


class Account(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True

    def __eq__(self, other):
        if isinstance(other, Account):
            return self.email == other.email and self.password == other.password