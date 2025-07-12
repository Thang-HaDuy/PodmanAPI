from typing import List
from pydantic import BaseModel


class PublishedPorts(BaseModel):
    host_ip: str      
    container_port: float
    host_port: float
    protocol: str


class ContainerSchema(BaseModel):
    id: str
    name: str
    state: str
    pod: str
    image: str
    created: str
    published_ports: List[PublishedPorts]


    class Config:
        from_attributes = True  # Cho phép ánh xạ từ đối tượng (nếu dùng ORM) 

