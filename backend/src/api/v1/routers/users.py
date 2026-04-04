from fastapi import APIRouter

router: APIRouter = APIRouter()


@router.get("")
async def get_cities() -> str:
    return "Sss"
