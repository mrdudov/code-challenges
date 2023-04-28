import pytest

from .data_set import data_set
from ..parse import parse_int


@pytest.mark.parametrize('test_item', data_set)
def test_base(test_item):
    assert parse_int(test_item["data"]) == test_item["result"]
