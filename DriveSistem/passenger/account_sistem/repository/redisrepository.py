
from typing import Optional

import redis
from pydantic import BaseModel


class RedisRepository:
    def __init__(self, url: str):
        self.redis = redis.from_url(url, decode_responses=True)

    def register_user(self, key_model: str, user: BaseModel, ttl_seconds: int = 100) -> None:
        key = key_model
        self.redis.set(key, user.json(), ex=ttl_seconds)

    def get_user(self, key_model: str, model: type[BaseModel]) -> Optional[BaseModel]:
        key = key_model
        user_data = self.redis.get(key)
        if user_data:
            return model.parse_raw(user_data)
        return None

    def delete_key(self, key_model: str) -> None:
        self.redis.delete(key_model)