import pytest
from fibonacci import fib
from .data_set import data_set


@pytest.mark.parametrize('test_item', data_set)
def test_brute_force_data_set(test_item):
    calculated_value = fib(test_item['value'])
    expected_value = test_item['result']

    assert calculated_value == expected_value
