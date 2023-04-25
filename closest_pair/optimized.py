from math import dist


def closest_pair_optimized(points):
    points = sorted(points, key=lambda p: p[0])
    # print_points(points)
    result = (points[0], points[1])
    min_dist = dist(*result)
    p_len = len(points)
    left_list = points[:p_len//2]
    right_list = points[p_len//2:]
    # print(f"{len(left_list)}")
    # print(f"{len(right_list)}")
    return result
