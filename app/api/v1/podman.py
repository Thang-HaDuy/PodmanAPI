from fastapi import APIRouter, Depends, HTTPException
from app.schemas.podman_info import GeneralInfoSchema
from app.services.container import PodmanContainerService, get_container_service
from app.services.image import PodmanImageService, get_images_service
from app.services.network import PodmanNetworkService, get_network_service
from app.services.pod import PodmanPodService, get_pod_service
from app.services.volume import PodmanVolumeService, get_volume_service

router = APIRouter()

@router.get("/podman-general-info", response_model=GeneralInfoSchema)
async def get_podman_general_info(
    container_service: PodmanContainerService = Depends(get_container_service),
    pod_service: PodmanPodService = Depends(get_pod_service),
    network_service: PodmanNetworkService = Depends(get_network_service),
    volume_service: PodmanVolumeService = Depends(get_volume_service),
    image_service: PodmanImageService = Depends(get_images_service),
):
    try:
        return {
            "total_containers": container_service.get_container_count(),
            "total_pods": pod_service.get_pod_count(),
            "total_networks": network_service.get_network_count(),
            "total_images": image_service.get_images_count(),
            "total_volumes": volume_service.get_volume_count(),
        }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e)) 