from battleship_field_validator import validate_battlefield
from data_set import data_set


if __name__ == '__main__':
    for test_item in data_set:
        calc_val = validate_battlefield(test_item['field'])
        print(f"{calc_val=}")
        print(f"is correct: {calc_val==test_item['is_valid']}")
