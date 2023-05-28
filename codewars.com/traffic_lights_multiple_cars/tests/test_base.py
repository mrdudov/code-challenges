import pytest

from .data_set import data_set
from ..traffic_lights_multiple_cars import traffic_lights


@pytest.mark.parametrize('test_item', data_set)
def test_base(test_item):
    assert traffic_lights(test_item["road"], test_item["n"]) == test_item["result"]
