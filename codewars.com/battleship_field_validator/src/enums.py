from enum import Enum


class Shape(Enum):
    HORIZONTAL = 1
    VERTICAL = 2
    SINGLE = 3


class FieldMark(Enum):
    SHIP = 1
    MARK_SHIP = 2
    CHECKED = 3


class Ships(Enum):
    BATTLESHIP = 1
    CRUISER = 2
    DESTROYER = 3
    SUBMARINE = 4
