from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.s3_client import S3Client
from app.config import settings

router = APIRouter()

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:    
        contents = await file.read()
        async with S3Client() as s3:
            await s3.put_object(
                Bucket=settings.S3_BUCKET_NAME,
                Key=file.filename,
                Body=contents,
                ContentType=file.content_type,
            )
        return {"filename": file.filename, "message": "Upload successful"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")
