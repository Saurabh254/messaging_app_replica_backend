from api.database.base_model import BaseModel
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String


class Users(BaseModel):
    name: Mapped[str] = mapped_column(String(255))
    profile_photo: Mapped[str] = mapped_column(String)
    phone: Mapped[str] = mapped_column(String, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
