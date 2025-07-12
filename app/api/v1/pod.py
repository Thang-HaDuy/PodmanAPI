from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.schemas.pod import PodSchema
from app.services.pod import PodmanPodService, get_pod_service

router = APIRouter()

@router.get("/list-pod", response_model=List[PodSchema])
async def list_pods(pod: PodmanPodService = Depends(get_pod_service)):
    try:
        return pod.get_list_pod()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))