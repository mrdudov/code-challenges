import pytest

from .data_set import data_set
from ..algorithm import kprimes_step


@pytest.mark.parametrize('test_item', data_set)
def test_base(test_item):
    assert kprimes_step(
        k=test_item["k"],
        step=test_item["step"],
        start=test_item["start"],
        nd=test_item["end"]
    ) == test_item["result"]
