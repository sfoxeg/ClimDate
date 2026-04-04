from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey
from core.models import Base
from core.models.mixins import IdPKMixin, CreatedAtMixin


class TokensOrm(IdPKMixin, CreatedAtMixin, Base):
    __tablename__ = "tokens"
    token: Mapped[String] = mapped_column(String, unique=True, index=True)
    user_id: Mapped[Integer] = mapped_column(Integer, ForeignKey("users.id"))
    user: Mapped["UsersOrm"] = relationship(back_populates="token")  # type: ignore[name-defined]
