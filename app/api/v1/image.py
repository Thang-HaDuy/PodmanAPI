from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.schemas.image import ImageSchema
from app.services.image import PodmanImageService, get_images_service

router = APIRouter()

@router.get("/list-image", response_model=List[ImageSchema])
async def list_pods(image: PodmanImageService = Depends(get_images_service)):
    try:
        return image.get_list_images()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))