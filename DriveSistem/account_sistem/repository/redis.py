from account_sistem.entity.email_confirmation import EmailConfirmation
from entity.user import User


class Redis:
    def __init__(self):
        self.users = {}

    def register_user(self, email_confirmation: EmailConfirmation, user: User) -> None:
        self.users.update({email_confirmation: user})

    def get_user(self, email_confirmation: EmailConfirmation) -> User | None:
        return self.users.get(email_confirmation)