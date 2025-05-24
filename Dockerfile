# Dockerfile
FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies
RUN apk update && apk add --no-cache \
    build-base \
    postgresql-dev \
    musl-dev \
    libffi-dev \
    gcc \
    cargo \
    libpq \
    linux-headers \
    jpeg-dev \
    zlib-dev

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the application
COPY ./app ./app
COPY ./app/main.py .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
