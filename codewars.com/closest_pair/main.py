from optimized import closest_pair_optimized

from src.functions import generate_test_points, print_run_time
from src.brute_force import closest_pair_brute_force


def main():
    points = generate_test_points(count=10, min_val=-1_000, max_val=1_000)
    closest_pair1 = print_run_time(closest_pair_brute_force)(points)
    closest_pair2 = print_run_time(closest_pair_optimized)(points)
    print("closest pair:")
    print(f"\t p1: {closest_pair1[0][0]:.3f}, {closest_pair2[0][1]:.3f}")
    print(f"\t p2: {closest_pair1[1][0]:.3f}, {closest_pair2[1][1]:.3f}")
    print(f"is v1 == v2: {closest_pair1==closest_pair2}")


if __name__ == "__main__":
    main()
