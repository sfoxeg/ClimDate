from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from core.models import Base
from core.models.mixins import IdPKMixin


class CitiesOrm(IdPKMixin, Base):
    __tablename__ = "cities"
    name: Mapped[str] = mapped_column(String(30), nullable=False)
