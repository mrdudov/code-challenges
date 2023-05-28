import pytest

from .data_set import data_set
from ..algorithm import dbl_linear


@pytest.mark.parametrize('test_item', data_set)
def test_base(test_item):
    assert dbl_linear(test_item["data"]) == test_item["result"]
