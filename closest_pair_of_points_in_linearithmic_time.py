import random
import time
from math import dist
from pprint import pprint

PRECISION = 3

def print_run_time(func):
    start = time.time()
    

def generate_test_points(count:int, min_val = -1000, max_val = 1000):
    result = []
    for _ in range(count):
        random_value_x = random.uniform(max_val, min_val)
        random_value_y = random.uniform(max_val, min_val)
        result.append((random_value_x, random_value_y))
    return result


def closest_pair(points):
    result = (points[0], points[1])
    min_dist = dist(*result)
    
    for i, point_a in enumerate(points):
        for j, point_b in enumerate(points):
            if i != j and dist(point_a, point_b) < min_dist:
                min_dist = dist(point_a, point_b)
                result = (point_a, point_b)
    return result

pprint(generate_test_points(count=1000, min_val=-10_000, max_val=10_000))
