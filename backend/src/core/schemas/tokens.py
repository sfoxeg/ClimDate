from pydantic import BaseModel, ConfigDict


class STokenAdd(BaseModel):
    token: str

    model_config = ConfigDict(from_attributes=True)


class SToken(STokenAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)


class STokenId(BaseModel):
    id: int
