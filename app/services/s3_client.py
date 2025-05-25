import aioboto3
from app.config import settings


class S3Client:
    def __init__(self):
        self.session = aioboto3.Session()

    async def __aenter__(self):
        self.client = await self.session.client(
            "s3",
            region_name=settings.AWS_REGION,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        ).__aenter__()
        return self.client

    async def __aexit__(self, exc_type, exc, tb):
        await self.client.__aexit__(exc_type, exc, tb)
