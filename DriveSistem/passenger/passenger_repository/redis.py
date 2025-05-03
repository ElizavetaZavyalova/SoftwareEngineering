from pydantic import BaseModel

from libs.tocken_generator.cryptography import Cryptography
from libs.tocken_generator.entity.account import Account, DEFAULT_PASSWORD
from passenger.account_sistem.repository.redisrepository import RedisRepository
from passenger.passenger.rest.passenger import Passenger


class PassengerRepositoryRedis(RedisRepository):
    def __init__(self, url: str):
        super().__init__(url=url)

    def register_user(self, email_confirmation: str, user: Passenger, **kwargs) -> None:
        return super().register_user(key_model=email_confirmation, user=user, ttl_seconds=100)

    def get_user(self, email_confirmation: str, **kwargs) -> Passenger | None:
        user = super().get_user(key_model=email_confirmation, model=Passenger)
        if user:
            super().delete_key(key_model=email_confirmation)
        return user

class PassengerCashRepositoryRedis(RedisRepository):
    def __init__(self, url: str):
        super().__init__(url=url)

    def get_user_profile(self, token: str) -> BaseModel | None:
        return super().get_user(key_model=token, model=Passenger)

    def user_profile_cashed(self, token: str, user: Passenger) -> None:
        return super().register_user(key_model=token, user=user, ttl_seconds=60 * 60 * 24)

    def change_user_profile(self, token: str, user: Passenger) -> None:
        super().delete_key(key_model=token)
        new_token = Cryptography().generate_token(account=Account(email=user.email,password=Cryptography().hash_password(user.password))).access_token
        user.password=DEFAULT_PASSWORD
        super().register_user(key_model=new_token, user=user, ttl_seconds=60 * 60 * 24)

    def delete_user_profile(self, token: str):
        super().delete_key(key_model=token)
