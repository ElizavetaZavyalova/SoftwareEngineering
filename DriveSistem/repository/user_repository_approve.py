from entity.user import UserContacts, User


class UserRepositoryApprove:
    def __init__(self):
        self.redis = {}

    def add_user(self, approve_code: int, user: UserContacts):
        self.redis[approve_code] = user
    def get_user_by_code(self, approve_code: int)->UserContacts:
        return self.redis.get(approve_code)