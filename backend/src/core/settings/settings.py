from pydantic_settings import BaseSettings
from .app_settings import AppSettings
from .db_settings import DBSettings


class Settings(BaseSettings):
    app: AppSettings = AppSettings()
    db: DBSettings = DBSettings()


settings = Settings()
