from sqlalchemy import Integer, String, Date
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


# Base class to ORM model
class Base(DeclarativeBase):
    pass


class CarPart(Base):
    __tablename__ = "car_part"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    car_name: Mapped[str] = mapped_column(String(100), nullable=False)
    part_name: Mapped[str] = mapped_column(String(100), nullable=False)
    interval: Mapped[int] = mapped_column(Integer, nullable=False)
    last_replacement: Mapped[Date] = mapped_column(Date, nullable=False)
    notes: Mapped[str] = mapped_column(String, nullable=True)
