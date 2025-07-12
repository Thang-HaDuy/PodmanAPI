from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.schemas.image import ImageSchema
from app.schemas.volume import VolumeSchema
from app.services.volume import PodmanVolumeService, get_volume_service

router = APIRouter()

@router.get("/list-volume", response_model=List[VolumeSchema])
async def list_volume(image: PodmanVolumeService = Depends(get_volume_service)):
    try:
        return image.get_list_volume()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))