from test_data import test_data
from simplifying import simplify


for test_case in test_data:
    
    print()
    print()
    print("*" * 80)
    print(f"equalities: {test_case['equalities']}")
    print(f"formula: {test_case['formula']}")
    print(f"expected answer: {test_case['answer']}")
    print("*" * 80)
    result = simplify(test_case["equalities"], test_case["formula"])
    print(f"{result=}")
    print(f"TEST PASSED: {result==test_case['answer']}")
