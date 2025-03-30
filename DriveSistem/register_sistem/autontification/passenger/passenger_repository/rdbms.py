from entity.account import Account
from register_sistem.autontification.repository.repositoryrdbms import RepositoryRDBMS
from entity.passenger import Passenger
from proxy.fake import generate_passenger


class PassengerRepositoryRDBMS(RepositoryRDBMS):
    def __init__(self):
        super().__init__()
    def init_proxy(self) -> dict:
        passengers = {p.email: p for p in [generate_passenger() for _ in range(5)]}
        for email, passenger in passengers.items():
            print(email, passenger, "\n")
        return passengers

    def register_user(self, user: Passenger) -> None:
        super().register_user(user)

    def find_user(self, email: str) -> bool:
        return super().find_user(email)

    def update_profile(self, account: Account, user: Passenger) -> bool:
        return super().update_profile(account, user)

    def delete_profile(self, account: Account, ) -> bool:
        return super().delete_profile(account)

    def get_user_by_email(self, email: str) -> Passenger | None:
        return super().get_user_by_email(email)

    def get_account(self, account: Account) -> Passenger | None:
        return super().get_account(account)

    def change_password(self, account: Account) -> bool:
        return super().change_password(account)

    def find_account(self, account: Account) -> bool:
        return super().find_account(account)
