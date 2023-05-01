import pytest

from ..src.brute_force import closest_pair_brute_force
from ..main import closest_pair_optimized
from .data_set import data_set


@pytest.mark.parametrize('test_item', data_set)
def test_brute_force_data_set(test_item):
    calculated_value = closest_pair_brute_force(test_item['points'])
    expected_value = tuple(test_item['result'])
    message = test_item['message']

    assert sorted(calculated_value) == sorted(expected_value), f"{message}"


@pytest.mark.parametrize('test_item', data_set)
def test_optimized_data_set(test_item):
    calculated_value = closest_pair_optimized(test_item['points'])
    expected_value = tuple(test_item['result'])
    message = test_item['message']

    assert sorted(calculated_value) == sorted(expected_value), f"{message}"
