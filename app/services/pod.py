import json
import logging
import subprocess
from fastapi import Depends
from podman import PodmanClient

from app.core.config import settings
from app.schemas.pod import PodSchema

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class PodmanPodService:
    def __init__(self):
        try:
            self.client = PodmanClient(base_url=settings.podman_socket)
            logger.debug("PodmanClient initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize PodmanClient: {str(e)}")
            raise
    def get_pod_count(self):
        pods = self.client.pods.list()
        return len(pods)
    
    def get_list_pod(self):
        pods = self.client.pods.list()
        return [
            PodSchema(
                id = p.id[:12],
                name = p.attrs.get("Name", "Unknown"),
                control = p.attrs.get("Cgroup", "Unknown"),
                namespace = p.attrs.get("Namespace", "Unknown"),
                total_container = len(p.attrs.get("Containers", [])),
                created = p.attrs.get("Created", "Unknown"),
                Status = p.attrs.get("Status", "Unknown"),
            )for p in pods
        ]
        

def get_pod_service():
    return PodmanPodService()