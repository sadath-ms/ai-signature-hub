# ai-signature-hub

docker-compose exec fastapi alembic revision --autogenerate -m "Add models"
docker-compose exec fastapi alembic upgrade head

psql -U myuser -d mydatabase

\dt