from fastapi import APIRouter
from fastapi.params import Depends
from api.v1.cities.repository import CitiesRepository
from api.v1.cities.schemas import SCity, SCityAdd, SCityId
from typing import Annotated

router: APIRouter = APIRouter()


@router.post("")
async def add_city(city: Annotated[SCityAdd, Depends()]) -> SCityId:
    return await CitiesRepository.add_one(city)


@router.get("")
async def get_cities() -> list[SCity]:
    return await CitiesRepository.find_all()
