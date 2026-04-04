import uuid

from fastapi import HTTPException
from sqlalchemy import select
from starlette import status
from core.database import new_session
from core.models import UsersOrm, TokensOrm
from core.schemas import SUserReg, SUserAuth, SUserId, STokenAdd
from core.secure import pwd_context


class AuthRepository:
    @classmethod
    async def reg_user(cls, data: SUserReg) -> SUserId:
        async with new_session() as session:
            creds_dict = data.model_dump()
            creds_dict.update({"password": pwd_context.hash(data.password)})
            user = UsersOrm(**creds_dict)
            session.add(user)
            await session.flush()
            await session.commit()
            return SUserId(id=user.id)

    @classmethod
    async def login(cls, data: SUserAuth) -> STokenAdd:
        async with new_session() as session:
            query = select(UsersOrm).where(UsersOrm.email == data.email)
            result = await session.execute(query)
            user = result.scalar_one_or_none()

            if not user:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="User not found",
                )
            if not pwd_context.verify(data.password, str(user.password)):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Incorrect password",
                )
            token = TokensOrm(user_id=user.id, token=str(uuid.uuid4()))
            session.add(token)
            await session.flush()
            await session.commit()
            return STokenAdd.model_validate({"token": token.token})
