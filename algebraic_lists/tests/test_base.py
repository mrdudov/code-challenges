from ..algebraic_lists import Cons


def test_create_list():
    """should create a list out of an array"""
    
    assert Cons.from_array([]) == None
    assert Cons.from_array([1,2,3,4,5]).to_array() == [1,2,3,4,5]

def test_filter():
    """should filter elements from a list"""

    assert Cons.from_array([1,2,3,4,5]).filter(lambda n: n > 3).to_array() == [4,5]
    assert Cons.from_array([1,2,3,4,5]).filter(lambda n: n > 5) == None


def test_create_transformed_list():
    """should create a new transformed list out of a source list"""

    assert Cons.from_array(["1","2","3","4","5"]).map(int).to_array() == [1,2,3,4,5]


def test_filter_transform():
    """should filter and transform a list here"""

    assert Cons.from_array([1,2,3,4,5]).filter(lambda n: n % 2 == 0).map(str).to_array() == ["2","4"]
