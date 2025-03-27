
from entity.user import UserContacts, User
class UserRepository:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserRepository, cls).__new__(cls)
        return cls._instance
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.db = {}
            self.initialized = True

    def get_user(self, email:str):
        return self.db.get(email)

    def add_user(self, user: UserContacts):
        self.db[user.email] = User(id=len(self.db) + 1,
                                    email=user.email,
                                    name=user.name,
                                    password=user.password, role=user.role,)

    def is_user_found(self, user_credit: UserContacts) -> bool:
        user = self.db[user_credit.email]
        if user is not None:
            if user.name == user_credit.name and user.password == user_credit.password:
                return True
        return False

    def is_user_registered(self, user: UserContacts) -> bool:
        return self.db.get(user.email) is not None