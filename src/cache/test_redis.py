from cache.redis_client import RedisClient

redis_client = RedisClient()

# Test cache
redis_client.set_cache("test_key", "Hello, Redis!")
value = redis_client.get_cache("test_key")

print(f"Cached Value: {value}")