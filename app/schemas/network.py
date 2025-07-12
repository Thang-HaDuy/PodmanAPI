from pydantic import BaseModel
from typing import List, Optional

class Subnet(BaseModel):
    subnet: str
    gateway: str

class NetworkSchema(BaseModel):
    id: str
    name: str
    driver: str
    ipv4: Optional[Subnet] = None
    ipv6: Optional[Subnet] = None

    class Config:
        from_attributes = True

