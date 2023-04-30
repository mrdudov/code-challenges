from tests.data_set import data_set
from algorithm import simplify


def main():
    
    print(f"equalities: {data_set[0]['equalities']}")
    print(f"formula: {data_set[0]['formula']}")
    print(f"expected result: {data_set[0]['result']}")
    print("*" * 80)
    result = simplify(data_set[0]["equalities"], data_set[0]["formula"])
    print(f"{result=}")
    print(f"TEST PASSED: {result==data_set[0]['result']}")


if __name__ == "__main__":
    main()
