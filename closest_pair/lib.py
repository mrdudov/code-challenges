import time
import functools


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
    print(f"({point[0]:.3f}, {point[1]:.3f})")


def print_points(points):
    print('Points:')
    for point in points:
        print('\t', end='')
        print_point(point)
