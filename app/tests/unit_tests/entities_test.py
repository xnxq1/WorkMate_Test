from app.domain.entities import *
import pytest

@pytest.mark.parametrize('id, name, normal_form', [
    ('b5a32451-5275-4c28-9e3e-851b5e4bd59d', 'Сфинкс', True),
    ('b5a42451-5275-4c28-9e3e-851b5e4bd59d', 'С' * 300, False),
])
async def test_breed(id, name, normal_form):
    try:
        breed = Breed(id=id, name=name)
        if not normal_form:
            assert False

        assert breed.name == name

    except:
        if normal_form:
            assert False


@pytest.mark.parametrize('id, name, color, age_in_month, normal_form', [
    ('b5a32451-5275-4c28-9e3e-851b5e4bd59d', 'Вася', Color.ginger, 5, True),
    ('b5a32421-5275-4c28-9e3e-851b5e4bd59d', 'Снежок', 'white', 10.0, False),
])
async def test_cat(id, name, color, age_in_month, normal_form):
    try:
        cat = Cat(id=id, name=name, color=color, age_in_month=age_in_month, breed_id='6f9bed9d-9c1a-4031-808f-3a8ff31157c1')
        if not normal_form:
            assert False
        assert cat.name == name
        assert cat.color == color
        assert cat.age_in_month == age_in_month
    except:
        if normal_form:
            assert False