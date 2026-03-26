from pydantic import BaseModel
from pydantic.networks import IPvAnyAddress


class AppSettings(BaseModel):
    host: IPvAnyAddress = "127.0.0.1"
    port: int = 8000
    reload: bool = True
