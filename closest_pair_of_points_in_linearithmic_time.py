import random
import time
import functools
from math import dist
from pprint import pprint

def print_run_time(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        print(f"function: {func.__name__} - {time.perf_counter() - start_time:.4f}")
        return value
    return wrapper


@print_run_time
def generate_test_points(count:int, min_val = -1_000, max_val = 1_000):
    result = []
    for _ in range(count):
        random_value_x = random.uniform(max_val, min_val)
        random_value_y = random.uniform(max_val, min_val)
        result.append((random_value_x, random_value_y))
    return result


@print_run_time
def closest_pair_v1(points):
    result = (points[0], points[1])
    min_dist = dist(*result)
    
    for i, point_a in enumerate(points):
        for j, point_b in enumerate(points):
            if i != j and dist(point_a, point_b) < min_dist:
                min_dist = dist(point_a, point_b)
                result = (point_a, point_b)
    return result


def print_point(point):
    print(f"({point[0]:.3f}, {point[1]:.3f})")


def print_points(points):
    print('Points:')
    for point in points:
        print('\t', end='')
        print_point(point)



@print_run_time
def closest_pair_v2(points):
    points = sorted(points, key=lambda p: p[0])
    # print_points(points)
    result = (points[0], points[1])
    min_dist = dist(*result)
    p_len = len(points)
    left_list = points[:p_len//2]
    right_list = points[p_len//2:]
    print(f"{len(left_list)}")
    print(f"{len(right_list)}")
    return result


def main():
    random.seed(123456)
    points = generate_test_points(count=3_000, min_val=-1_000, max_val=1_000)
    closest_pair1 = closest_pair_v1(points)
    closest_pair2 = closest_pair_v2(points)
    print("closest pair:")
    print(f"\t p1: {closest_pair1[0][0]:.3f}, {closest_pair2[0][1]:.3f}")
    print(f"\t p2: {closest_pair1[1][0]:.3f}, {closest_pair2[1][1]:.3f}")
    print(f"is v1 == v2: {closest_pair1==closest_pair2}")


if __name__ == "__main__":
    main()
