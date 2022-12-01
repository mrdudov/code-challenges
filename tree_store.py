from pprint import pprint


class TreeStore:

    def __init__(self, items):
        self._store = {item["id"]: item for item in items}

    def getAll(self):
        return list(self._store.values())

    def getItem(self, id):
        return self._store[id]

    def getChildren(self, id):
        return [item for item in self._store.values() if item["parent"] == id]

    def getAllParents(self, id):
        result = []
        current_id = id
        current_item = self._store[current_id]

        while True:
            current_id = current_item["parent"]
            current_item = self._store[current_id]
            result.append(current_item)
            if current_item["parent"] == "root":
                break

        return result


items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]


ts = TreeStore(items)


pprint(ts.getAll())
ts.getAll() == [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]


print(f"{ts.getItem(7)=}")
ts.getItem(7) == {"id": 7, "parent": 4, "type": None}


print(f"{ts.getChildren(4)=}")
ts.getChildren(4) == [
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]

print(f"{ts.getChildren(5)=}")
ts.getChildren(5) == []


pprint(ts.getAllParents(7))
ts.getAllParents(7) == [
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 1, "parent": "root"}
]
