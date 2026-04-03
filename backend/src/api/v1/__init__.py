__all__ = ["router"]


from fastapi import APIRouter

from core.settings import settings
from .cities.router import router as cities_router
from .users.router import router as users_router

router: APIRouter = APIRouter()
router.include_router(
    cities_router,
    prefix=settings.app.api.v1.cities.prefix,
    tags=settings.app.api.v1.cities.tags,
)
router.include_router(
    users_router,
    prefix=settings.app.api.v1.users.prefix,
    tags=settings.app.api.v1.users.tags,
)
