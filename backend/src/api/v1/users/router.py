from fastapi import APIRouter


router: APIRouter = APIRouter()


@router.get("")
async def get_cities():
    return "await UsersRepository.find_all()"
