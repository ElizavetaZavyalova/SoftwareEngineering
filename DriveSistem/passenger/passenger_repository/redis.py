from libs.account_sistem.entity.email_confirmation import EmailConfirmation
from libs.account_sistem.repository.redis import Redis
from libs.entity.passenger.rest.passenger import Passenger


class PassengerRepositoryRedis(Redis):
    def __init__(self):
        super().__init__()
    def register_user(self, email_confirmation: EmailConfirmation, user: Passenger) -> None:
        return super().register_user(email_confirmation=email_confirmation, user=user)

    def get_user(self, email_confirmation: EmailConfirmation) -> Passenger | None:
        return super().get_user(email_confirmation=email_confirmation)
