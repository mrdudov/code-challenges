import pytest

from .data_set import data_set
from ..algorithm import validate_battlefield


@pytest.mark.parametrize('test_item', data_set)
def test_battleship_field_validator(test_item):
    calculated_value = validate_battlefield(test_item["field"])
    expected_value = test_item["is_valid"]
    message = test_item["message"]

    assert calculated_value == expected_value, message
