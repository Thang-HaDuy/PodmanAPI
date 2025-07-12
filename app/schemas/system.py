from pydantic import BaseModel

class SystemInfo(BaseModel):
    cpu_count: int
    memory_total: float  # Tổng RAM (GB)
    memory_used: float   # RAM đã sử dụng (GB)
    kernel_version: str
    podman_version: str