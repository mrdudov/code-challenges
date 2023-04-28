import pytest

from .dataset import data_set
from ..voting import runoff


@pytest.mark.parametrize('test_item', data_set)
def test_base(test_item):
    assert runoff(test_item['data']) == test_item['result']
