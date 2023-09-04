from sqlalchemy import JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class Rooms(Base):
    __tablename__ = "rooms"

    id: Mapped[int] = mapped_column(primary_key=True)
    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotels.id"))
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    price: Mapped[int] = mapped_column(nullable=False)
    services: Mapped[list[str]] = mapped_column(JSON)
    quantity: Mapped[int] = mapped_column(nullable=False)
    image_id: Mapped[int] = mapped_column(nullable=False)

