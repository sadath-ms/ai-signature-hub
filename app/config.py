from pydantic import BaseSettings

class Settings(BaseSettings):
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    ELASTICSEARCH_HOST: str = "http://localhost:9200"

    class Config:
        env_file = ".env"

settings = Settings()
