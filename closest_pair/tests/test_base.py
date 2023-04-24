from lib import closest_pair_brute_force


def test_data_set(get_data_set):
    for test_item in get_data_set:
        calculated_value = closest_pair_brute_force(test_item['points'])
        expected_value = tuple(test_item['result'])
        message = test_item['message']

        assert sorted(calculated_value) == sorted(expected_value), f"{message}"

