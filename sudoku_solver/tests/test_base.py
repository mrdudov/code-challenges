import pytest

from .data_set import data_set
from ..sudoku_solver import sudoku_solver


@pytest.mark.parametrize('test_item', data_set)
def test_base(test_item):
    assert sudoku_solver(test_item["puzzle"]) == test_item["result"], test_item["message"]
