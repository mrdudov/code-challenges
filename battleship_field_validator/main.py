from validator import validate_battlefield
from tests.data_set import data_set


if __name__ == '__main__':
    test_item = data_set[0]
    calc_val = validate_battlefield(test_item['field'])
    print(f"{calc_val=}")
    print(f"is correct: {calc_val==test_item['is_valid']}")
