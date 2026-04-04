from fastapi import APIRouter
from fastapi.params import Depends
from starlette import status
from typing import Annotated
from core.repositories import CitiesRepository
from core.schemas import SCityId, SCity, SCityAdd

router: APIRouter = APIRouter()


@router.post("", status_code=status.HTTP_201_CREATED)
async def add_city(city: Annotated[SCityAdd, Depends()]) -> SCityId:
    return await CitiesRepository.add_one(city)


@router.get("")
async def get_cities() -> list[SCity]:
    return await CitiesRepository.find_all()
