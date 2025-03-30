from entity.account import Account
from account_sistem.repository.repositoryrdbms import RepositoryRDBMS
from entity.driver import Driver
from proxy.fake import generate_driver


class DriverRepositoryRDBMS(RepositoryRDBMS):
    def __init__(self):
        super().__init__()
    def init_proxy(self) -> dict:
        drivers = {p.email: p for p in [generate_driver() for _ in range(5)]}
        for email, driver in drivers.items():
            print(email, driver, "\n")
        return drivers

    def register_user(self, user: Driver) -> None:
        super().register_user(user)

    def find_user(self, email: str) -> bool:
        return super().find_user(email)

    def update_profile(self, account: Account, user: Driver) -> bool:
        return super().update_profile(account, user)

    def delete_profile(self, account: Account, ) -> bool:
        return super().delete_profile(account)

    def get_user_by_email(self, email: str) -> Driver | None:
        return super().get_user_by_email(email)

    def get_account(self, account: Account) -> Driver | None:
        return super().get_account(account)

    def change_password(self, account: Account) -> bool:
        return super().change_password(account)

    def find_account(self, account: Account) -> bool:
        return super().find_account(account)