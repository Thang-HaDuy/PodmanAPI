import json
import logging
from typing import Dict, List, Optional
import psutil
import subprocess
from podman import PodmanClient
from fastapi import Depends
from app.core.config import settings
from app.schemas.network import NetworkSchema, Subnet

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class PodmanNetworkService:
    def __init__(self):
        
        try:
            self.client = PodmanClient(base_url=settings.podman_socket)
            logger.debug("PodmanClient initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize PodmanClient: {str(e)}")
            raise

    def get_network_count(self):
        try:
            networks = self.client.networks.list()
            return len(networks)
        except Exception as e:
            logger.error(f"Error counting networks: {str(e)}")
            raise

    def get_list_network(self):
        networks = self.client.networks.list(all=True)
        for c in networks: 
            print(json.dumps(c.attrs, indent=2))
        return [
            NetworkSchema(
                id = n.id,
                name = n.attrs.get("name", "Unknown"),
                driver = n.attrs.get("driver", "Unknown"),
                ipv4=self._parse_subnets(n.attrs.get("subnets", []))[0],
                ipv6=self._parse_subnets(n.attrs.get("subnets", []))[1],
            )for n in networks
        ]

    def _parse_subnets(self, subnets: List[Dict]) -> tuple[Optional[Subnet], Optional[Subnet]]:
        """Phân tích subnets để lấy thông tin IPv4 và IPv6, không phụ thuộc thứ tự."""
        ipv4 = None
        ipv6 = None
        for subnet in subnets:
            subnet_str = subnet.get("subnet", "")
            gateway = subnet.get("gateway", "")
            # Kiểm tra IPv4 (chứa dấu chấm)
            if "." in subnet_str:
                ipv4 = Subnet(subnet=subnet_str, gateway=gateway)
            # Kiểm tra IPv6 (chứa dấu hai chấm)
            elif ":" in subnet_str:
                ipv6 = Subnet(subnet=subnet_str, gateway=gateway)
        return ipv4, ipv6
def get_network_service():
    return PodmanNetworkService()