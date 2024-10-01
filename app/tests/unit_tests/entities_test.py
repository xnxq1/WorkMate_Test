from app.domain.entities import *
import pytest

@pytest.mark.parametrize('name, size, activity, normal_form', [
    ('Сфинкс', Size.big, Activity.active, True),
    ('Сфинкс', 'big', 'active', False),
])
async def test_breed(name, size, activity, normal_form):
    try:
        breed = Breed(name=name, size=size, activity=activity)
        if not normal_form:
            assert False
        assert breed.name == name
        assert breed.size == size
        assert breed.activity == activity
    except:
        if normal_form:
            assert False


@pytest.mark.parametrize('name, color, age_in_month, normal_form', [
    ('Вася', Color.ginger, 5, True),
    ('Снежок', 'white', 10.0, False),
])
async def test_cat(name, color, age_in_month, normal_form):
    try:
        cat = Cat(name=name, color=color, age_in_month=age_in_month)
        if not normal_form:
            assert False
        assert cat.name == name
        assert cat.color == color
        assert cat.age_in_month == age_in_month
    except:
        if normal_form:
            assert False