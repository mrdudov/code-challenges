from .data_set import data_set
from lib import closest_pair_brute_force


def test_data_set():
    for test_item in data_set:
        calculatet_value = closest_pair_brute_force(test_item['points'])
        expected_value = tuple(test_item['result'])
        message = test_item['message']

        assert sorted(calculatet_value) == sorted(expected_value), f"{message}"
