from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.schemas.image import ImageSchema
from app.schemas.network import NetworkSchema
from app.services.network import PodmanNetworkService, get_network_service

router = APIRouter()

@router.get("/list-network", response_model=List[NetworkSchema])
async def list_pods(image: PodmanNetworkService = Depends(get_network_service)):
    try:
        return image.get_list_network()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))