import pytest

from .data_set import data_set
from ..algorithm import simplify


@pytest.mark.parametrize('test_item', data_set)
def test_base(test_item):
    assert simplify(test_item["equalities"], test_item["formula"]) == test_item["result"]
