from pydantic import BaseModel
from typing import List

class ImageSchema(BaseModel):
    id: str
    unused: bool
    tag: List[str]
    size: str
    created: str

    class Config:
        from_attributes = True