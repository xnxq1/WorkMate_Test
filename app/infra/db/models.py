from sqlalchemy import CheckConstraint, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Relationship

from app.domain.entities import Color
from uuid import UUID, uuid4


class Base(DeclarativeBase):
    pass

class Breed(Base):
    __tablename__ = 'Breed'

    id: Mapped[UUID] = mapped_column(primary_key=True, unique=True, default=uuid4)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)

    __table_args__ = (
        CheckConstraint('length(name) <= 255', name='check_name_max_length'),
        CheckConstraint('length(name) > 0', name='check_name_min_length'),
    )


class Cat(Base):
    __tablename__ = 'Cat'

    id: Mapped[UUID] = mapped_column(primary_key=True, unique=True, default=uuid4)
    name: Mapped[str] = mapped_column(nullable=False)
    color: Mapped[Color] = mapped_column(nullable=False)
    age_in_month: Mapped[int] = mapped_column(nullable=False)
    breed_id: Mapped[UUID] = mapped_column(ForeignKey('Breed.id', ondelete='cascade'))

    __table_args__ = (
        CheckConstraint('length(name) <= 255', name='check_name_max_length'),
        CheckConstraint('length(name) > 0', name='check_name_min_length'),
        CheckConstraint('age_in_month > 0', name='check_age_in_month_min_value')
    )