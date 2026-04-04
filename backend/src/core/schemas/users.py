from datetime import datetime

from pydantic import BaseModel, EmailStr, ConfigDict


class SUserAuth(BaseModel):
    email: EmailStr
    password: str


SUserReg = SUserAuth


class SUser(SUserAuth):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class SUserId(BaseModel):
    id: int
