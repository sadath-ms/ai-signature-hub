from fastapi import FastAPI
from app.services.redis_service import redis_client
from app.services.elastic_service import elastic
from app.routers import upload

app = FastAPI(title="FastAPI S3 File Upload")

app.include_router(upload.router)

# app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI running with PostgreSQL, Redis, and Elasticsearch"}

@app.get("/redis")
def redis_test():
    redis_client.set("test_key", "Hello from Redis")
    return {"redis_value": redis_client.get("test_key").decode()}

@app.get("/elastic")
def elastic_test():
    return elastic.info()
