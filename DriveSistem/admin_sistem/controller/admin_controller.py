from fastapi import HTTPException

from admin_sistem.repository.admin_repository import AdminRepository
from libs.tocken_generator.cryptography import Cryptography
from libs.tocken_generator.entity.account import Account


class AdminController:
    _LOG_IN = 'Вход'

    def __init__(self, admin_repository: AdminRepository):
        self.admins = admin_repository

    def login(self, account: Account):
        account.password = Cryptography().hash_password(password=account.password)
        if self.admins.is_admin(account):
            token = Cryptography().generate_token(account=account)
            return token
        raise HTTPException(status_code=400, detail="Incorrect username or password")
