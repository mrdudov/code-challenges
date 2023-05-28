import pytest

from .data_set import data_set
from ..algorithm import permutation_free


@pytest.mark.parametrize('test_item', data_set)
def test_base(test_item):
    assert permutation_free(test_item['n'], test_item["l"]) == test_item["result"]
