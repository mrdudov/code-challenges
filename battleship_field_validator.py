# https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/train/python

from enum import Enum
from collections import Counter


battleField = [
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
]


def validate_battlefield(field):

    field_len = len(field)
    ships = []

    class Shape(Enum):
        HORIZONTAL = 1
        VERTICAL = 2
        SINGLE = 3

    class ShapeException(Exception):
        pass

    def get_ship(i, j):
        shape = detect_shape(i, j)
        result = [(i, j)]
        if shape == Shape.SINGLE:
            return result
        while True:
            if shape == Shape.HORIZONTAL:
                j += 1
            elif shape == Shape.VERTICAL:
                i += 1
            else:
                raise ShapeException('unexpected shape of ship')
            try:
                if field[i][j] == 1:
                    result.append((i, j))
                else:
                    break
            except IndexError:
                break
        return result

    def get_ship_perimetr(coordinates):
        result = set()

        i_coords = [coord[0] for coord in coordinates]
        j_coords = [coord[1] for coord in coordinates]
        i_min = min(i_coords)
        i_max = max(i_coords)
        j_min = min(j_coords)
        j_max = max(j_coords)

        for i in range(i_min-1, i_max+1+1):
            for j in range(j_min-1, j_max+1+1):
                if 0 <= i < field_len and 0 <= j < field_len:
                    result.add((i, j))
        return list(result - set(coordinates))

    def mark_as_cheked(coordinates):
        for i, j in coordinates:
            field[i][j] = 4

    def detect_shape(i, j):
        try:
            if field[i][j+1] == 1:
                return Shape.HORIZONTAL
        except:
            pass
        try:
            if field[i+1][j] == 1:
                return Shape.VERTICAL
        except:
            pass
        return Shape.SINGLE

    def is_ship_perimetr_clean(coordinates):
        for i, j in coordinates:
            if field[i][j] == 1:
                return False
        return True

    def mark_ship(coordinates):
        for i, j in coordinates:
            field[i][j] = 2

    for i, line in enumerate(field):
        for j, val in enumerate(line):
            if val == 1:
                ship = get_ship(i, j)
                ships.append(len(ship))
                mark_ship(ship)
                perimetr = get_ship_perimetr(ship)
                if not is_ship_perimetr_clean(perimetr):
                    return False
                mark_as_cheked(perimetr)
    ship_counter = Counter(ships)
    if ship_counter != {1: 4, 2: 3, 3: 2, 4: 1}:
        return False
    return True


if __name__ == '__main__':
    print(f"{validate_battlefield(battleField)=}")
