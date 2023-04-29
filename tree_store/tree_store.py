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
