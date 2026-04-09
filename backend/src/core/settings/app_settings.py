import os
from pydantic import BaseModel
from core.settings.api_settings import APISettings


class AppSettings(BaseModel):
    host: str = os.environ.get("APP_HOST", "127.0.0.1")
    port: int = int(os.environ.get("APP_PORT", 8000))
    reload: bool = bool(os.environ.get("APP_RELOAD", False))
    log_level: str = os.environ.get("APP_LOG_LEVEL", "INFO")
    cors_allow: str = os.environ.get("APP_CORS_ALLOW", "*")
    api: APISettings = APISettings()
