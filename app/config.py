from pydantic import BaseSettings

class Settings(BaseSettings):
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    ELASTICSEARCH_HOST: str = "http://localhost:9200"

    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_REGION: str = "ap-southeast-2"  # default if you want
    S3_BUCKET_NAME: str
    

    class Config:
        env_file = ".env"

settings = Settings()
