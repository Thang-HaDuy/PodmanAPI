from podman import PodmanClient
from fastapi import Depends
from app.core.config import settings
import json

class PodmanService:
    def __init__(self):
        # Kết nối với Podman qua socket
        self.client = PodmanClient(base_url=settings.podman_socket)

    def list_containers(self):
        containers = self.client.containers.list(all=True)
        for c in containers: 
            print(json.dumps(c.attrs, indent=2))
        return [
            {
                "id": c.id[:12],  # Lấy 12 ký tự đầu của ID
                "state": c.attrs["State"] if c.attrs["State"] else "Unknown",
                "name": c.name,
                "status": c.status
            }
            for c in containers
        ]

    def start_container(self, container_id: str):
        container = self.client.containers.get(container_id)
        container.start()

    def stop_container(self, container_id: str):
        container = self.client.containers.get(container_id)
        container.stop()

    def list_pods(self):
        pods = self.client.pods.list()
        return [
            {
                "id": p.id[:12],
                "name": p.attrs["Name"],
                "status": p.attrs["Status"],
                "containers": [c["Id"] for c in p.attrs.get("Containers", [])]
            }
            for p in pods
        ]
    
    def total_container(self):
        total_container = self.client.containers.count()
        return {"total_container": total_container}

# Dependency để inject PodmanService
def get_podman_service():
    return PodmanService()