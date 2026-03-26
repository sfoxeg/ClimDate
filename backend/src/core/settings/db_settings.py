import os
from pydantic import BaseModel


class DBSettings(BaseModel):
    __host: str = os.environ.get("POSTGRES_HOST", "localhost")
    __dbname: str = os.environ.get("POSTGRES_DB", "climdate")
    __user: str = os.environ.get("POSTGRES_USER", "pgtest")
    __password: str = os.environ.get("POSTGRES_PASSWORD", "pgtest")
    __port: str = os.environ.get("POSTGRES_PORT", "5432")
    url: str = (
        f"postgresql+asyncpg://{__user}:{__password}@{__host}:{__port}/{__dbname}"
    )
    expire_on_commit: bool = False
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
