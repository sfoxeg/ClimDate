from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from core.settings import settings

engine = create_async_engine(
    settings.db.url,
    echo=settings.db.echo,
    echo_pool=settings.db.echo_pool,
    pool_size=settings.db.pool_size,
    max_overflow=settings.db.max_overflow
)

new_session = async_sessionmaker(
    engine,
    expire_on_commit=settings.db.expire_on_commit
)
