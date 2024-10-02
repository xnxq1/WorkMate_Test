from app.domain.entities import *
import pytest

@pytest.mark.parametrize('id, name, normal_form', [
    (1, 'Сфинкс', True),
    (2, 'С' * 300, False),
])
async def test_breed(id, name, normal_form):
    try:
        breed = Breed(id=id, name=name)
        if not normal_form:
            assert False

        assert breed.id == id
        assert breed.name == name

    except:
        if normal_form:
            assert False


@pytest.mark.parametrize('id, name, color, age_in_month, normal_form', [
    (1, 'Вася', Color.ginger, 5, True),
    (2, 'Снежок', 'white', 10.0, False),
])
async def test_cat(id, name, color, age_in_month, normal_form):
    try:
        cat = Cat(id=id, name=name, color=color, age_in_month=age_in_month)
        if not normal_form:
            assert False
        assert cat.name == name
        assert cat.color == color
        assert cat.age_in_month == age_in_month
    except:
        if normal_form:
            assert False