from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.schemas.container import ContainerSchema
from app.services.container import PodmanContainerService, get_container_service

router = APIRouter()

@router.get("/list-container", response_model=List[ContainerSchema])
async def list_containers(container: PodmanContainerService = Depends(get_container_service)):
    try:
        return container.get_list_container()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/containers/{container_id}/start")
async def start_container(container_id: str, podman: PodmanContainerService = Depends(get_container_service)):
    try:
        podman.start_container(container_id)
        return {"status": "started"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/containers/{container_id}/stop")
async def stop_container(container_id: str, podman: PodmanContainerService = Depends(get_container_service)):
    try:
        podman.stop_container(container_id)
        return {"status": "stopped"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))