from test_data import test_data
from simplifying import simplify


for test_case in test_data:
    print('*'*60)
    print(f"equalities: {test_case['equalities']}")
    print(f"formula: {test_case['formula']}")
    print(f"expected answer: {test_case['answer']}")
