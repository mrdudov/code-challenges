import time
import functools
import random

from math import dist
from itertools import combinations


def print_run_time(func):
    """Print the runtime of the decorated function"""
   
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        print(f"function: {func.__name__} - {time.perf_counter() - start_time:.4f}")
        return value
    return wrapper


def print_point(point):
    """Print single point"""
    
    print(f"({point[0]:.3f}, {point[1]:.3f})")


def print_points(points):
    """Print points list"""
    
    print('Points:')
    for point in points:
        print('\t', end='')
        print_point(point)


def generate_test_points(count:int, min_val = -1_000, max_val = 1_000, seed = 123456):
    """Generate random points"""
   
    random.seed(seed)
    result = []
    for _ in range(count):
        random_value_x = random.uniform(max_val, min_val)
        random_value_y = random.uniform(max_val, min_val)
        result.append((random_value_x, random_value_y))
    return result


def closest_pair_brute_force(points):
    """Closest pair brute force"""
    
    result = (points[0], points[1])
    min_dist = dist(*result)
    
    for pair in combinations(points, r=2):
        if dist(*pair) < min_dist:
            min_dist = dist(*pair)
            result = pair
    return result
