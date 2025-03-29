from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str
    host: str
    port: int

    # Database Config
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_password: str

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