# https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/train/python

from pprint import pprint


def validate_battlefield(field):
    pprint(field)

    battleship_count = 1
    cruiser_count = 1
    destroyer_count = 3
    submarine_count = 4

    def mark_as_cheked(i1, j1, i2, j2):
        pass

    def detect_direction(i, j):
        if field[i][j+1] == 1:
            return 'v'
        if field[i+1][j] == 1:
            return 'g'
        return 's'

    def get_ship_size(i, j):
        ship_direction = detect_direction(i, j)
        print(f"{ship_direction=}")
        if ship_direction == 's':
            return 1
        if ship_direction == 'v':
            size = 0
            for n in range(i, len(field[j])):
                if field[i][n] == 1:
                    size += 1
                else:
                    return size
        if ship_direction == 'g':
            size = 0
            for n in range(j, len(field)):
                if field[n][j] == 1:
                    size += 1
                else:
                    return size

    for i, line in enumerate(field):
        for j, val in enumerate(line):
            if val == 1:
                ship_size = get_ship_size(i, j)
                print(f"{ship_size=}")

    return True
