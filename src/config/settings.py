from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "AI-Powered-Chatbot"
    host: str = "0.0.0.0"
    port: int = 8000

    # Database settings
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_password: str

    # Kafka settings
    kafka_broker: str
    kafka_topic: str = "chat-messages"

    # Redis settings
    redis_host: str
    redis_port: int

    class Config:
        env_file = ".env"

settings = Settings()