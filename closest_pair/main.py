from math import dist

from . import lib


@lib.print_run_time
def closest_pair_optimized(points):
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
    points = lib.generate_test_points(count=3_000, min_val=-1_000, max_val=1_000)
    closest_pair1 = lib.closest_pair_brute_force(points)
    closest_pair2 = closest_pair_optimized(points)
    print("closest pair:")
    print(f"\t p1: {closest_pair1[0][0]:.3f}, {closest_pair2[0][1]:.3f}")
    print(f"\t p2: {closest_pair1[1][0]:.3f}, {closest_pair2[1][1]:.3f}")
    print(f"is v1 == v2: {closest_pair1==closest_pair2}")


if __name__ == "__main__":
    main()

