import os
from pydantic import BaseModel


class AppSettings(BaseModel):
    host: str = os.environ.get("HOST", "127.0.0.1")
    port: int = int(os.environ.get("PORT", 8000))
    reload: bool = bool(os.environ.get("RELOAD", False))
    log_level: str = os.environ.get("LOG_LEVEL", "INFO")
