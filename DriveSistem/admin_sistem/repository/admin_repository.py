from entity.account import Account


class AdminRepository:
    def __init__(self):
        self.admins = {'admin@mail.ru': Account(email='admin@mail.ru', password='admin')}

    def is_admin(self, admin: Account) -> bool:
        account = self.admins.get(admin.email)
        return account and account.email == admin.email

