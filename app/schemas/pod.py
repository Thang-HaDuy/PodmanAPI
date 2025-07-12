from pydantic import BaseModel
from typing import List

class PodSchema(BaseModel):
    id: str
    name: str
    control: str
    namespace: str
    total_container: float
    created: str
    Status: str

    class Config:
        from_attributes = True