from pydantic import BaseModel, ConfigDict


class SCityAdd(BaseModel):
    name: str


class SCity(SCityAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)


class SCityId(BaseModel):
    id: int
