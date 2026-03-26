from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column


class CreatedAtMixin:
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class UpdatedAtMixin:
    updated_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)