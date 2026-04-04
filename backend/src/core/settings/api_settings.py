from enum import Enum
from pydantic import BaseModel


class Route(BaseModel):
    prefix: str = ""
    tags: list[str | Enum] = []


class APIv1Settings(Route):
    name: str = "API v1"
    version: str = "v1"
    prefix: str = f"/{version}"
    tags: list[str | Enum] = [name, version]

    """Параметры ручек"""
    cities: Route = Route(prefix="/cities", tags=["Города"])
    auth: Route = Route(prefix="/auth", tags=["Аутентификация"])
    users: Route = Route(prefix="/users", tags=["Пользователи"])


class APISettings(Route):
    """Основной роутер"""

    prefix: str = "/api"
    tags: list[str | Enum] = ["api"]

    """Подключение очередной версии API"""
    v1: APIv1Settings = APIv1Settings()
