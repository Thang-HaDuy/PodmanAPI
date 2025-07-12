from pydantic import BaseModel
from typing import List

class VolumeSchema(BaseModel):
    name: str
    driver: str
    mountpoint: str
    created: str

    class Config:
        from_attributes = True