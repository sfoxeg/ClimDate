import os
from pydantic import BaseModel
from ipaddress import IPv4Address


class AppSettings(BaseModel):
    __ip: IPv4Address = IPv4Address(os.environ.get("HOST", "127.0.0.1"))
    host: str = str(__ip)
    port: int = int(os.environ.get("PORT", 8000))
    reload: bool = bool(os.environ.get("RELOAD", False))
    log_level: str = os.environ.get("LOG_LEVEL", "INFO")
