import enum
from uuid import uuid4, UUID

from pydantic import BaseModel, ConfigDict, Field





class Color(enum.Enum):
    white = 'white'
    gray = 'gray'
    black = 'black'
    ginger = 'ginger'


class Breed(BaseModel):
    id: UUID = Field(default_factory=uuid4, kw_only=True)
    name: str = Field(min_length=0, max_length=255)

    model_config = ConfigDict(
        from_attributes=True
    )


class Cat(BaseModel):
    id: UUID = Field(default_factory=uuid4, kw_only=True)
    name: str = Field(min_length=0, max_length=255)
    color: Color
    age_in_month: int = Field(gt=0)
    breed_id: UUID

    model_config = ConfigDict(
        from_attributes=True
    )