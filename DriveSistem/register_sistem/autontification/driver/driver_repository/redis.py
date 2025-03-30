from register_sistem.autontification.entity.email_confirmation import EmailConfirmation
from register_sistem.autontification.repository.redis import Redis
from register_sistem.autontification.driver.driver import Driver


class DriverRepositoryRedis(Redis):
    def __init__(self):
        super().__init__()

    def register_user(self, email_confirmation: EmailConfirmation, user: Driver) -> None:
        return super().register_user(email_confirmation=email_confirmation, user=user)

    def get_user(self, email_confirmation: EmailConfirmation) -> Driver | None:
        return super().get_user(email_confirmation=email_confirmation)
