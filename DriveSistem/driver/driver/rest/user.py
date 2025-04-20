from pydantic import constr

from libs.tocken_generator.entity.account import Account


class User(Account):
    first_name: constr(pattern=r"^[A-Za-zА-Яа-яЁё]{2,50}$")
    last_name: constr(pattern=r"^[A-Za-zА-Яа-яЁё]{2,50}$")
    patronymic: constr(pattern=r"^[A-Za-zА-Яа-яЁё]{2,50}$")
    phone_number: constr(pattern=r'^\+?\d{10,15}$')

    class Config:
        orm_mode = True

    def name(self):
        return self.first_name+" "+self.patronymic+" "+self.last_name