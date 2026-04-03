from datetime import datetime
from typing import Optional
from sqlalchemy import Boolean, Enum, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column
from core.models import Base
from core.models.mixins import IdPKMixin, CreatedAtMixin, UpdatedAtMixin
from core.types import BanStatus


class UsersOrm(IdPKMixin, CreatedAtMixin, UpdatedAtMixin, Base):
    __tablename__ = "users"
    email: Mapped[String] = mapped_column(String(100))
    password: Mapped[String] = mapped_column(String(100))
    is_active: Mapped[bool] = mapped_column(
        Boolean, default=False, server_default="False", nullable=False
    )
    is_admin: Mapped[bool] = mapped_column(
        Boolean, default=False, server_default="False", nullable=False
    )
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, server_default="False", nullable=False
    )
    banned_status: Mapped[BanStatus] = mapped_column(
        Enum(
            BanStatus,
            name="ban_status",
            values_callable=lambda obj: [e.value for e in obj],
        ),
        default=BanStatus.NOT_BANNED.value,
        server_default=BanStatus.NOT_BANNED.value,
        nullable=False,
    )
    banned_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    banned_description: Mapped[Optional[String]] = mapped_column(String, nullable=True)
