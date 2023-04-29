from .data_set import items


def test_det_all_method(get_ts):
    assert get_ts.getAll() == items


def test_det_item_method(get_ts):
    assert get_ts.getItem(7) == {
        "id": 7, "parent": 4, "type": None
    }


def test_det_children_method(get_ts):
    assert get_ts.getChildren(4) == [
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type": None}
    ]
    assert get_ts.getChildren(5) == []


def test_det_all_parents_method(get_ts):
    assert get_ts.getAllParents(7) == [
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 1, "parent": "root"}
    ]
