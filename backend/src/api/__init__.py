__all__ = ["router"]


from fastapi import APIRouter
from api.v1 import router as api_v1_router
from core.settings import settings

router: APIRouter = APIRouter(
    prefix=settings.app.api.prefix, tags=settings.app.api.tags
)

router.include_router(
    api_v1_router, prefix=settings.app.api.v1.prefix, tags=settings.app.api.v1.tags
)
