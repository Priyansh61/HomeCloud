from fastapi import APIRouter, UploadFile, File, Depends
from app.services.minio_client import client, BUCKET_NAME
from app.auth.auth_bearer import JWTBearer
import datetime

router = APIRouter()

@router.post("/files/upload", dependencies=[Depends(JWTBearer())])
async def upload_file(file: UploadFile = File(...)):
    timestamp = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")
    object_name = f"{timestamp}_{file.filename}"

    client.put_object(
        BUCKET_NAME,
        object_name,
        file.file,
        length=-1,  # Let MinIO auto-detect size
        part_size=10 * 1024 * 1024,
        content_type=file.content_type
    )

    return {"message": "File uploaded successfully", "filename": object_name}
