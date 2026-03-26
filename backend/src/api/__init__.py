from fastapi import APIRouter
from .v1 import router as api_v1_router

router: APIRouter = APIRouter(prefix='/api', tags=['api'])
router.include_router(api_v1_router, prefix='/v1', tags=['v1'])
