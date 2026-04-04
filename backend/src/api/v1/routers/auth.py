from typing import Annotated
from fastapi import APIRouter, Depends
from starlette import status
from core.repositories import AuthRepository
from core.schemas import SUserId, STokenAdd
from core.schemas.users import SUserAuth, SUserReg

router: APIRouter = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(user: Annotated[SUserReg, Depends()]) -> SUserId:
    return await AuthRepository.reg_user(user)


@router.post("/login", status_code=status.HTTP_201_CREATED)
async def login(user: Annotated[SUserAuth, Depends()]) -> STokenAdd:
    return await AuthRepository.login(user)
