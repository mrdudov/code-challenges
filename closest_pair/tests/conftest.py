import pytest

from .data_set import data_set


@pytest.fixture
def get_data_set():
    return data_set
