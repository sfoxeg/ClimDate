from pydantic_settings import BaseSettings
from core.settings import AppSettings, DBSettings


class Settings(BaseSettings):
    app: AppSettings = AppSettings()
    db: DBSettings = DBSettings()
