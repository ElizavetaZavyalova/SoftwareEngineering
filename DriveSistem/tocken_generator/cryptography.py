import secrets
from jose import jwt

from tocken_generator.entity.token import Token
from entity.account import Account

class Cryptography:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):
            self.key = secrets.token_hex(32)
            print(self.key)
            self.algorithm = "HS256"
            self._initialized = True

    def generate_confirm_code(self) -> str:
        code = secrets.token_hex(5)
        return code

    def generate_token(self, account: Account) -> Token:
        token = jwt.encode(account.model_dump(), key=self.key, algorithm=self.algorithm)
        return Token(access_token=token, token_type='bearer')

    def decrypt_token(self, token: str) -> Account:
        account = jwt.decode(token=token, key=self.key, algorithms=[self.algorithm])
        return Account(**account)
