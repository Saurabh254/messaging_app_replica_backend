from sqlalchemy.orm import declarative_mixin, Mapped, declared_attr, mapped_column
from sqlalchemy import Column, Integer, String, DateTime
from nanoid import generate
from datetime import datetime
from .db import Base


@declarative_mixin
class MyMixin:
    id: Mapped[str] = mapped_column(
        String(12), default=lambda: generate(size=12), primary_key=True, unique=True
    )
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[DateTime] = Column(
        DateTime, default=datetime.now, onupdate=datetime.now
    )

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    __table_args__ = {"mysql_engine": "InnoDB"}
    __mapper_args__ = {"always_refresh": True}

    id = Column(Integer, primary_key=True)


class BaseModel(MyMixin, Base): ...
