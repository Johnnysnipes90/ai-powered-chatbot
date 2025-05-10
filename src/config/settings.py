from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str
    host: str
    port: int

    # PostgreSQL Config
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str
    postgres_port: int

    # Kafka Config
    kafka_broker: str
    kafka_topic: str

    # Redis Config
    redis_host: str
    redis_port: int
    redis_db: int
    redis_ttl: int

    class Config:
        env_file = ".env"


settings = Settings()