from fastapi import FastAPI
from app.api.v1 import container, image, pod, podman, system, network, volume

app = FastAPI(
    title="Podman Manager API",
    description="A simple API to manage Podman containers, pods, and system info",
    version="0.1.0"
)

app.include_router(container.router, prefix="/api/v1", tags=["container"])
app.include_router(pod.router, prefix="/api/v1", tags=["pods"])
app.include_router(system.router, prefix="/api/v1", tags=["system"])
app.include_router(podman.router, prefix="/api/v1", tags=["podman"])
app.include_router(image.router, prefix="/api/v1", tags=["image"])
app.include_router(network.router, prefix="/api/v1", tags=["network"])
app.include_router(volume.router, prefix="/api/v1", tags=["volume"])

@app.get("/")
async def root():
    return {"message": "Welcome to Podman Manager API"}