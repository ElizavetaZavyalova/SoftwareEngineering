from fastapi import HTTPException

from libs.email.entity.email_confirmation import EmailConfirmation
from libs.email.send_email import EmailSender
from libs.tocken_generator.cryptography import Cryptography
from libs.tocken_generator.entity.account import Account
from passenger.account_sistem.repository.redisrepository import RedisRepository
from passenger.account_sistem.repository.repositoryrdbms import RepositoryRDBMS
from passenger.passenger.rest.passenger import Passenger
from passenger.passenger.rest.user import User
from passenger.passenger_repository.redis import PassengerRepositoryRedis, PassengerCashRepositoryRedis


class Tags:
    _REGISTER = 'Регистрация'
    _LOG_IN = 'Вход'
    _PROFILE_SETTINGS = 'Настройки профиля'
    _PASSWORD_RECOVERY = 'Востановление пароля'




class Controller:
    def __init__(self, redis: PassengerRepositoryRedis, rdbms: RepositoryRDBMS, cash:PassengerCashRepositoryRedis):
        self.redis = redis
        self.rdbms = rdbms
        self.cash=cash

    def register_user(self, user: User):
        user.password = Cryptography().hash_password(password=user.password)
        if not self.rdbms.find_user(email=user.email):
            confirm_code = Cryptography().generate_confirm_code()
            email_confirmation = EmailConfirmation(confirm_code=confirm_code, email=user.email)
            self.redis.register_user(email_confirmation=str(email_confirmation), user=user)
            EmailSender().send_approve_register_email(email_confirmation=email_confirmation)
            return {'status': 'success', 'message': f'Check your email {user.email}'}
        raise HTTPException(status_code=400, detail='Passenger already exists')

    def confirm_email(self, email_confirmation: EmailConfirmation):
        user = self.redis.get_user(email_confirmation=str(email_confirmation))
        if user:
            self.rdbms.register_user(user=user)
            EmailSender().send_welcome_email(email=user.email, user=user.name())
            return {'status': 'success', 'message': f'Registered {repr(user)}'}
        raise HTTPException(status_code=400, detail='Invalid confirmation code or passenger not found')

    def forgot_password(self, account: Account):
        user = self.rdbms.get_user_by_email(email=account.email)
        if user:
            user.password = Cryptography().hash_password(password=account.password)
            confirm_code = Cryptography().generate_confirm_code()
            email_confirmation = EmailConfirmation(confirm_code=confirm_code, email=account.email)
            self.redis.register_user(email_confirmation=str(email_confirmation), user=user)
            EmailSender().send_approve_chenge_password_email(email_confirmation=email_confirmation)
            return {'status': 'success', 'message': f'Check your email: {user.email}'}
        raise HTTPException(status_code=400, detail='Account not found')

    def change_password(self, email_confirmation: EmailConfirmation):
        user = self.redis.get_user(email_confirmation=str(email_confirmation))
        if user and self.rdbms.change_password(account=user):
            EmailSender().send_change_password_email(email=user.email, user=user.name())
            return {'status': 'success', 'message': f'Password changed for {repr(user)}'}
        raise HTTPException(status_code=400, detail='Invalid confirmation code or passenger not found')

    def login(self, account: Account):
        account.password = Cryptography().hash_password(password=account.password)
        if self.rdbms.find_account(account=account):
            token = Cryptography().generate_token(account=account)
            return token
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    def get_user_profile(self, token: str):
        user = self.cash.get_user_profile(token=token)
        if user:
            return user
        account = Cryptography().decrypt_token(token)
        user = self.rdbms.get_account(account=account)
        if user:
            self.cash.user_profile_cashed(token=token, user=user)
            return user
        raise HTTPException(status_code=400, detail="Profile not found")

    def change_user_profile(self, user: User, token: str):
        account = Cryptography().decrypt_token(token)
        user.password = Cryptography().hash_password(password=user.password)
        if self.rdbms.update_profile(account=account, user=user):
            self.cash.change_user_profile(token, user=user)
            return {'status': 'success', 'message': f'Profile was change {repr(user)}'}
        raise HTTPException(status_code=400, detail=f"{user.email} is already use")

    def delete_profile(self, token: str):
        account = Cryptography().decrypt_token(token)
        if self.rdbms.delete_profile(account=account):
            self.cash.delete_user_profile(token)
            return {'status': 'success', 'message': f'Profile was delete'}
        raise HTTPException(status_code=400, detail=f"account not found")
