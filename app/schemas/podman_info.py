from pydantic import BaseModel

class GeneralInfoSchema(BaseModel):
    total_pods: float
    total_containers: float
    total_images: float
    total_volumes: float
    total_networks: float

    class Config:
        from_attributes = True  # Cho phép ánh xạ từ đối tượng (nếu dùng ORM) 