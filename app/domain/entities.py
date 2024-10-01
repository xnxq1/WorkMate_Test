import enum

from pydantic import BaseModel

class Size(enum.Enum):
    small = 'small'
    average = 'average'
    big = 'big'

class Activity:
    active = 'active'
    inactive = 'inactive'



class Color(enum.Enum):
    white = 'white'
    gray = 'gray'
    black = 'black'
    ginger = 'ginger'


class Breed(BaseModel):
    name: str
    size: Size
    activity: Activity

    class Config:
        orm_mode = True


class Cat(BaseModel):
    name: str
    color: Color
    age_in_month: int

    class Config:
        orm_mode = True