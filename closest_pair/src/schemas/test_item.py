from pydantic import BaseModel

from src.common_types import Point, Points
from typing import Tuple


class TestItem(BaseModel):
    message: str
    points: Points
    result: Tuple[Point, Point]
