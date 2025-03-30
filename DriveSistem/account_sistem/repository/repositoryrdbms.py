from entity.account import Account
from entity.user import User


class RepositoryRDBMS:
    def __init__(self):
        self.users = self.init_proxy()

    def init_proxy(self) -> dict:
        pass  # TODO remove

    def register_user(self, user: User) -> None:
        if self.find_user(user.email):
            raise ValueError(f"Пользователь с email {user.email} уже зарегистрирован.")
        self.users[user.email] = user

    def find_user(self, email: str) -> bool:
        return email in self.users

    def update_profile(self, account: Account, user: User) -> bool:
        if account.email == user.email:
            self.users.update({account.email:user})
            return True
        if self.find_user(user.email):
            return False
        del self.users[account.email]
        self.users.update({user.email: user})
        return True

    def delete_profile(self, account: Account,) -> bool:
        if self.find_user(account.email):
            del self.users[account.email]
            return True
        return False
    def get_user_by_email(self, email: str) ->User | None:
        return self.users.get(email)

    def get_account(self, account:Account) -> User | None:
        return self.users.get(account.email)

    def change_password(self, account: Account) -> bool:
        user = self.users.get(account.email)
        if user:
            user.password = account.password
            self.users.update({account.email: user})
            return True
        return False

    def find_account(self, account: Account) -> bool:
        user = self.users.get(account.email)
        return user and user.password == account.password