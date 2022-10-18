# https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/train/python

from pprint import pprint
from enum import Enum


battleField = [
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


def validate_battlefield(field):

    class Direction(Enum):
        HORIZONTAL = 1
        VERTICAL = 2
        SINGLE = 3

    battleship_count = 1
    cruiser_count = 1
    destroyer_count = 3
    submarine_count = 4

    def get_ship(i, j):
        direction = detect_direction(i, j)
        result = [(i, j)]
        if direction == Direction.SINGLE:
            return result
        while True:
            if direction == Direction.HORIZONTAL:
                j += 1
            if direction == Direction.VERTICAL:
                i += 1
            try:
                if field[i][j] == 1:
                    result.append((i, j))
                else:
                    break
            except:
                break
        return result

    def get_ship_perimetr_coordinates(i1, j1, i2, j2, direction):

        result = []
        n = len(field)

        i_start = i1 - 1 if i1 > 0 else 0
        i_end = i2 + 1 if i2 < n else n
        j_start = j1 - 1 if j1 > 0 else 0
        j_end = j2 + 1 if j2 < n else n

        for i in range(i_start, i_end+1):
            for j in range(j_start, j_end+1):
                result.append((i, j))
        return result

    def mark_as_cheked(coordinates):
        for coordinate in coordinates:
            field[coordinate[0]][coordinate[1]] = 4

    def detect_direction(i, j):
        if field[i][j+1] == 1:
            return Direction.HORIZONTAL
        if field[i+1][j] == 1:
            return Direction.VERTICAL
        return Direction.SINGLE

    def get_ship_size(i, j):
        ship_direction = detect_direction(i, j)
        if ship_direction == Direction.SINGLE:
            return i, j, i, j, ship_direction
        if ship_direction == Direction.VERTICAL:
            size = 0
            for n in range(i, len(field)):
                if field[n][j] == 1:
                    size += 1
                else:
                    return i, j, i + size - 1, j, ship_direction
        if ship_direction == Direction.HORIZONTAL:
            size = 0
            for n in range(j, len(field[0])):
                if field[i][n] == 1:
                    size += 1
                else:
                    return i, j, i, j + size - 1, ship_direction

    def is_ship_perimetr_clean(coordinates):
        for coordinate in coordinates:
            if field[coordinate[0]][coordinate[1]] == 1:
                return False
        return True

    def mark_ship(i1, j1, i2, j2, direction):
        if direction == Direction.VERTICAL:
            for k in range(i1, i2 + 1):
                field[k][j1] = 2
        if direction == Direction.HORIZONTAL:
            for k in range(j1, j2 + 1):
                field[i1][k] = 2
        if direction == Direction.SINGLE:
            field[i1][j1] = 2

    for i, line in enumerate(field):
        for j, val in enumerate(line):
            if val == 1:
                ship_size = get_ship_size(i, j)
                mark_ship(*ship_size)
                perimetr = get_ship_perimetr_coordinates(*ship_size)
                if not is_ship_perimetr_clean(perimetr):
                    return False
                mark_as_cheked(perimetr)
    return True


if __name__ == '__main__':
    print(f"{validate_battlefield(battleField)=}")
