import random

import pytest
from faker import Faker
from faker_education import SchoolProvider
from faker_education.constants import school_list

fake = Faker()
fake.add_provider(SchoolProvider)


@pytest.fixture
def schools():
    return school_list


school_keys = ["school", "district", "level", "type", "state", "nces_id"]


def test_schools(schools):
    assert len(schools) > 1


@pytest.mark.parametrize("test_input", school_keys)
def test_dict_keys(schools, test_input):
    a = random.choice(schools)
    assert test_input in a.keys()


def test_school_name():
    name = fake.school_name()
    assert len(name) > 2


def test_school_district():
    district = fake.school_district()
    assert len(district) > 2


def test_school_level():
    level = fake.school_level()
    assert len(level) > 2


def test_school_type():
    school_type = fake.school_type()
    assert len(school_type) >= 1


def test_school_state():
    state = fake.school_state()
    assert len(state) == 2


def test_school_nces_id():
    nces_id = fake.school_nces_id()
    assert len(nces_id) in (11, 12)
