import json
import logging
from podman import PodmanClient
from fastapi import Depends
from app.core.config import settings
from app.schemas.volume import VolumeSchema

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class PodmanVolumeService:
    def __init__(self):
        
        try:
            self.client = PodmanClient(base_url=settings.podman_socket)
            logger.debug("PodmanClient initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize PodmanClient: {str(e)}")
            raise

    def get_volume_count(self):
        volumes = self.client.volumes.list(all=True)
        return len(volumes)
    
    def get_list_volume(self):
        volume = self.client.volumes.list()
        return [
            VolumeSchema(
                name = v.attrs.get("Name", "Unknown"),
                driver = v.attrs.get("Driver", "Unknown"),
                mountpoint = v.attrs.get("Mountpoint", "Unknown"),
                created = v.attrs.get("CreatedAt", "Unknown"),
            )for v in volume
        ]

def get_volume_service():
    return PodmanVolumeService()