from fastapi import APIRouter, Depends, HTTPException
from app.schemas.system import SystemInfo
from app.services.system import SystemService

router = APIRouter()

@router.get("/system-info", response_model=SystemInfo)
async def get_system_info(podman: SystemService = Depends()):
    try:
        return podman.get_system_info()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))