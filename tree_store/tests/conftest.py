import pytest

from .data_set import items
from ..tree_store import TreeStore


@pytest.fixture
def get_ts():
    return TreeStore(items)
