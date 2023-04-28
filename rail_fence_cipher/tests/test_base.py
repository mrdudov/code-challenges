import pytest

from .data_set import data_set
from ..rail_fence_cipher import decode_rail_fence_cipher, encode_rail_fence_cipher


@pytest.mark.parametrize('test_item', data_set)
def test_base(test_item):
    if test_item["type"] == 'encode':
        assert encode_rail_fence_cipher(test_item["data"], test_item["length"]) == test_item["result"]
    if test_item["type"] == 'decode':
        assert decode_rail_fence_cipher(test_item["data"], test_item["length"]) == test_item["result"]
