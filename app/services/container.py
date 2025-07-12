import json
import logging
from podman import PodmanClient
from fastapi import Depends
from app.core.config import settings
from app.schemas.container import ContainerSchema, PublishedPorts

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class PodmanContainerService:
    def __init__(self):
        
        try:
            self.client = PodmanClient(base_url=settings.podman_socket)
            logger.debug("PodmanClient initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize PodmanClient: {str(e)}")
            raise

    def get_container_count(self):
        containers = self.client.containers.list(all=True)
        return len(containers)

    def get_list_container(self):
        containers = self.client.containers.list(all=True)
        # for c in containers: 
        #     print(json.dumps(c.attrs, indent=2))
        return [
            ContainerSchema(
                id = c.id[:12],  # Lấy 12 ký tự đầu của ID
                name = c.attrs.get("Names", ["Unknown"])[0] if c.attrs.get("Names") else "Unknown",
                state = c.attrs.get("State", "Unknown"),
                pod = c.attrs.get("PodName", "Unknown"),
                image = c.attrs.get("Image", "Unknown"),
                created = c.attrs.get("Created", "Unknown"),
                published_ports = self._get_container_ports(c),
            )for c in containers
        ]
    

    def _get_container_ports(self, container):
        ports = container.attrs.get("Ports", [])
        if not ports:
            return []  # Trả về danh sách rỗng nếu không có cổng
        return [
            PublishedPorts(
                host_ip = port.get("host_ip", ""),
                container_port = port.get("container_port", 0),
                host_port = port.get("host_port", 0),
                protocol = port.get("protocol", "Unknown")
            )for port in ports
        ]

def get_container_service():
    return PodmanContainerService()