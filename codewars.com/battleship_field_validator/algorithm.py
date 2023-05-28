from collections import Counter

from src.enums import Shape, FieldMark
from src.exceptions import ShapeException
from configure import SHIPS_COUNT


def is_ships_count(ships):
    ship_counter = Counter(ships)
    if ship_counter != SHIPS_COUNT:
        return False
    return True


def validate_battlefield(field):

    field_len = len(field)
    ships = []

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
                if field[i][j] == FieldMark.SHIP.value:
                    result.append((i, j))
                else:
                    break
            except IndexError:
                break
        return result

    def get_ship_perimeter(coordinates):
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

    def mark_as_checked(coordinates):
        for i, j in coordinates:
            field[i][j] = FieldMark.CHECKED.value

    def detect_shape(i, j):
        try:
            if field[i][j+1] == FieldMark.SHIP.value:
                return Shape.HORIZONTAL
        except:
            pass
        try:
            if field[i+1][j] == FieldMark.SHIP.value:
                return Shape.VERTICAL
        except:
            pass
        return Shape.SINGLE

    def is_ship_perimeter_clean(coordinates):
        for i, j in coordinates:
            if field[i][j] == FieldMark.SHIP.value:
                return False
        return True

    def mark_ship(coordinates):
        for i, j in coordinates:
            field[i][j] = FieldMark.MARK_SHIP.value

    for i, line in enumerate(field):
        for j, val in enumerate(line):
            if val == FieldMark.SHIP.value:
                ship = get_ship(i, j)
                ships.append(len(ship))
                mark_ship(ship)
                perimeter = get_ship_perimeter(ship)
                if not is_ship_perimeter_clean(perimeter):
                    return False
                mark_as_checked(perimeter)
    
    if not is_ships_count(ships=ships):
        return False
    
    return True
