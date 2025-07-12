from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Podman Manager"
    podman_socket: str
    secret_key: str  # Thêm trường secret_key
    database_url: str  # Thêm trường database_url

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()