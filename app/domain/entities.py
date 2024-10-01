import enum

from pydantic import BaseModel, ConfigDict, Field


class Size(enum.Enum):
    small = 'small'
    average = 'average'
    big = 'big'

class Activity(enum.Enum):
    active = 'active'
    inactive = 'inactive'



class Color(enum.Enum):
    white = 'white'
    gray = 'gray'
    black = 'black'
    ginger = 'ginger'


class Breed(BaseModel):
    name: str = Field(min_length=0, max_length=255)
    size: Size
    activity: Activity

    model_config = ConfigDict(
        from_attributes=True
    )


class Cat(BaseModel):
    name: str = Field(min_length=0, max_length=255)
    color: Color
    age_in_month: int = Field(gt=0)

    model_config = ConfigDict(
        from_attributes=True
    )