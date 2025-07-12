import logging
import psutil
import subprocess
from podman import PodmanClient
from fastapi import Depends
from app.core.config import settings

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class SystemService:
    def __init__(self):
        
        try:
            self.client = PodmanClient(base_url=settings.podman_socket)
            logger.debug("PodmanClient initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize PodmanClient: {str(e)}")
            raise

    def get_system_info(self):
        try:
            # Lấy thông tin CPU
            cpu_count = psutil.cpu_count(logical=True)

            # Lấy thông tin RAM (chuyển sang GB)
            memory = psutil.virtual_memory()
            memory_total = memory.total / (1024 ** 3)  # Chuyển từ bytes sang GB
            memory_used = memory.used / (1024 ** 3)

            # Lấy phiên bản kernel
            kernel_version = subprocess.run(
                ["uname", "-r"],
                capture_output=True,
                text=True,
                check=True
            ).stdout.strip()

            # Lấy phiên bản Podman
            podman_version = subprocess.run(
                ["podman", "--version"],
                capture_output=True,
                text=True,
                check=True
            ).stdout.strip().replace("podman version ", "")

            return {
                "cpu_count": cpu_count,
                "memory_total": round(memory_total, 2),
                "memory_used": round(memory_used, 2),
                "kernel_version": kernel_version,
                "podman_version": podman_version
            }
        except Exception as e:
            logger.error(f"Error getting system info: {str(e)}")
            raise

def get_system_service():
    return SystemService()