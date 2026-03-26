from fastapi import APIRouter
from .cities.router import router as cities_router
from .users.router import router as users_router


router: APIRouter = APIRouter()
router.include_router(cities_router, prefix="/cities", tags=["Города"])
router.include_router(users_router, prefix="/users", tags=["Пользователи"])
