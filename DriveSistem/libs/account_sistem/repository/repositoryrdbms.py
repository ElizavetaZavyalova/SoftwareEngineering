from libs.entity.account import Account
from libs.entity.user import User


class RepositoryRDBMS:

    def register_user(self, user: User) -> None:
        pass

    def find_user(self, email: str) -> bool:
        pass

    def update_profile(self, account: Account, user: User) -> bool:
        pass

    def delete_profile(self, account: Account,) -> bool:
        pass
    def get_user_by_email(self, email: str) ->User | None:
        pass

    def get_account(self, account:Account) -> User | None:
        pass

    def change_password(self, account: Account) -> bool:
        pass

    def find_account(self, account: Account) -> bool:
        pass