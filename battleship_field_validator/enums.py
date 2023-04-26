from enum import Enum


class Shape(Enum):
    HORIZONTAL = 1
    VERTICAL = 2
    SINGLE = 3


class FieldMark(Enum):
    SHIP = 1
    MARK_SHIP = 2
    CHECKED = 4
