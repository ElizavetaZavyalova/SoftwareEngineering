from fastapi import HTTPException

from entity.user import User
from tocken_generator.cryptography import Cryptography
from entity.account import Account
from account_sistem.entity.email_confirmation import EmailConfirmation
from account_sistem.repository.redis import Redis
from account_sistem.email.send_email import EmailSender


class Tags:
    _REGISTER = 'Регистрация'
    _LOG_IN = 'Вход'
    _PROFILE_SETTINGS = 'Настройки профиля'
    _PASSWORD_RECOVERY = 'Востановление пароля'

class Controller:
    def __init__(self, redis: Redis, rdbms):
        self.redis = redis
        self.rdbms = rdbms

    def register_user(self, user: User):
        if not self.rdbms.find_user(email=user.email):
            confirm_code = Cryptography().generate_confirm_code()
            email_confirmation = EmailConfirmation(confirm_code=confirm_code, email=user.email)
            self.redis.register_user(email_confirmation=email_confirmation, user=user)
            EmailSender().send_approve_register_email(email_confirmation=email_confirmation)
            return {'status': 'success', 'message': f'Check your email {user.email}'}
        raise HTTPException(status_code=400, detail='Passenger already exists')

    def confirm_email_passenger(self, email_confirmation: EmailConfirmation):
        user = self.redis.get_user(email_confirmation=email_confirmation)
        if user:
            self.rdbms.register_user(user=user)
            EmailSender().send_welcome_email(user=user)
            return {'status': 'success', 'message': f'Registered {repr(user)}'}
        raise HTTPException(status_code=400, detail='Invalid confirmation code or passenger not found')

    def forgot_password(self, account: Account):
        user = self.rdbms.get_user_by_email(email=account.email)
        if user:
            confirm_code = Cryptography().generate_confirm_code()
            email_confirmation = EmailConfirmation(confirm_code=confirm_code, email=account.email)
            self.redis.register_user(email_confirmation=email_confirmation, user=user)
            EmailSender().send_approve_chenge_password_email(email_confirmation=email_confirmation)
            return {'status': 'success', 'message': f'Check your email: {user.email}'}
        raise HTTPException(status_code=400, detail='Account not found')

    def change_password(self, email_confirmation: EmailConfirmation):
        user = self.redis.get_user(email_confirmation=email_confirmation)
        if user and self.rdbms.change_password(account=user):
            EmailSender().send_change_password_email(user=user)
            return {'status': 'success', 'message': f'Password changed for {repr(user)}'}
        raise HTTPException(status_code=400, detail='Invalid confirmation code or passenger not found')

    def login(self, account: Account):
        if self.rdbms.find_account(account=account):
            token = Cryptography().generate_token(account=account)
            return token
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    def get_user_profile(self, token: str):
        account = Cryptography().decrypt_token(token)
        user = self.rdbms.get_account(account=account)
        if user:
            return user
        raise HTTPException(status_code=400, detail="Profile not found")

    def change_user_profile(self, user: User, token: str):
        account = Cryptography().decrypt_token(token)
        if self.rdbms.update_profile(account=account, user=user):
            return {'status': 'success', 'message': f'Profile was change {repr(user)}'}
        raise HTTPException(status_code=400, detail=f"{user.email} is already use")

    def delete_profile(self, token: str):
        account = Cryptography().decrypt_token(token)
        if self.rdbms.delete_profile(account=account):
            return {'status': 'success', 'message': f'Profile was delete'}
        raise HTTPException(status_code=400, detail=f"account not found")
