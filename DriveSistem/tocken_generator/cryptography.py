import os
import secrets
from jose import jwt
import bcrypt

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
            self.key = os.getenv('TOKEN_SECRET', secrets.token_hex(32))
            print('TOKEN_SECRET='+self.key)
            self.algorithm = os.getenv('ALGO_SECRET', "HS256")
            self.salt = os.getenv('SALT_SECRET', "$2b$12$abcdefghijklmnopqrstuu")
            print('ALGO_SECRET=' + self.algorithm)
            self._initialized = True

    def generate_confirm_code(self) -> str:
        code = secrets.token_hex(5)
        return code

    def hash_password(self, password: str) -> str:
        return bcrypt.hashpw(password.encode('utf-8'), self.salt.encode("utf-8")).decode('utf-8')[len(self.salt):]

    def generate_token(self, account: Account) -> Token:
        token = jwt.encode(account.model_dump(), key=self.key, algorithm=self.algorithm)
        return Token(access_token=token, token_type='bearer')

    def decrypt_token(self, token: str) -> Account:
        account = jwt.decode(token=token, key=self.key, algorithms=[self.algorithm])
        return Account(**account)
