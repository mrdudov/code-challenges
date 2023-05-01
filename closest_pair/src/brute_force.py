from math import dist
from itertools import combinations

from .common_types import Points, Point

def closest_pair_brute_force(points: Points) -> Point:
    """Closest pair brute force"""
    
    result = (points[0], points[1])
    min_dist = dist(*result)
    
    for pair in combinations(points, r=2):
        if dist(*pair) < min_dist:
            min_dist = dist(*pair)
            result = pair
    return result
