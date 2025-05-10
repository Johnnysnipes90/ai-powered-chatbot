import redis
import logging
from src.config.settings import settings

logging.basicConfig(level=logging.INFO)

class RedisClient:
    def __init__(self):
        self.client = redis.StrictRedis(
            host=settings.redis_host,
            port=settings.redis_port,
            db=settings.redis_db,
            decode_responses=True
        )

    def set_cache(self, key: str, value: str, ttl=None):
        ttl = ttl or settings.redis_ttl
        self.client.setex(key, ttl, value)
        logging.info(f"Cached data for key: {key}")

    def get_cache(self, key: str):
        value = self.client.get(key)
        if value:
            logging.info(f"Cache hit for key: {key}")
        else:
            logging.info(f"Cache miss for key: {key}")
        return value