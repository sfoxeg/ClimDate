from sqlalchemy import select
from core.models import CitiesOrm
from core.database import new_session
from api.v1.cities.schemas import SCityAdd, SCity, SCityId


class CitiesRepository:
    @classmethod
    async def add_one(cls, data: SCityAdd) -> SCityId:
        async with new_session() as session:
            city_dict = data.model_dump()
            city = CitiesOrm(**city_dict)
            session.add(city)
            await session.flush()
            await session.commit()
            return SCityId(id=city.id)

    @classmethod
    async def find_all(cls) -> list[SCity]:
        async with new_session() as session:
            query = select(CitiesOrm)
            result = await session.execute(query)
            cities_models = result.scalars().all()
            cities_schemas = [
                SCity.model_validate(city_model) for city_model in cities_models
            ]
            return cities_schemas
