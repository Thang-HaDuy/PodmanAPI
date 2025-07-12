import json
import logging
from podman import PodmanClient
from fastapi import Depends
from app.core.config import settings
from app.schemas.image import ImageSchema
from datetime import datetime
import pytz

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class PodmanImageService:
    def __init__(self):
        
        try:
            self.client = PodmanClient(base_url=settings.podman_socket)
            logger.debug("PodmanClient initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize PodmanClient: {str(e)}")
            raise

    def get_images_count(self):
        images = self.client.images.list(all=True)
        return len(images)

    def get_list_images(self):
        images = self.client.images.list(all=True)
        for c in images: 
            print(json.dumps(c.attrs, indent=2))
        return [
            ImageSchema(
                id = i.id,
                tag = i.attrs.get("RepoTags", "Unknown"),
                unused = True if i.attrs.get("Containers", 0) > 0 else False,
                size = self._format_size(i.attrs.get("Size", 0)),
                created = datetime.fromtimestamp(i.attrs.get("Created", 0), tz=pytz.timezone('Asia/Ho_Chi_Minh')).isoformat(),
            )for i in images
        ]
    def _format_size(self, size: int) -> str:
        """Chuyển đổi size từ byte sang GB, MB, hoặc byte."""
        if size >= 1024**3:  # GB
            return f"{size / (1024**3):.2f} GB"
        elif size >= 1024**2:  # MB
            return f"{size / (1024**2):.2f} MB"
        return f"{size} bytes"

def get_images_service():
    return PodmanImageService()