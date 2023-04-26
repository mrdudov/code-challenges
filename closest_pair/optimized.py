from math import dist
from itertools import combinations

from lib import print_points

all_points = []


def min_pair(points):
    return min(
        [
            {
                "dist":dist(*pair), 
                "pair": pair
            } 
            for pair in combinations(points, r=2)
        ], 
        key=lambda d: d["dist"]
    )["pair"]


def closest_pair_optimized(points, left=0, right=0, is_first_call = True):
    """closest pair optimized"""
    
    global all_points
    
    data_set_len = len(points)
     
    if is_first_call:
        points = sorted(points, key=lambda p: p[0])
        left = 0
        right = data_set_len
        all_points = points   
    
    print('')
    print_points(points)

    if data_set_len <= 1:
        raise ValueError('points count less then two')
        
    if data_set_len == 2:
        result = points

    if data_set_len == 3:
        result = min_pair(points)
    
    if data_set_len >= 4:

        left_left = left
        left_right = (right+left)//2

        right_left = (right+left)//2 
        right_right = right

        left_list = all_points[left_left:left_right]
        right_list = all_points[right_left:right_right]

        left_result = closest_pair_optimized(
            points=left_list, 
            left=left_left,
            right=left_right,
            is_first_call=False
        )
        
        right_result = closest_pair_optimized(
            points=right_list,
            left=right_left,
            right=right_right,
            is_first_call=False
        )
        
        # result = left_result if dist(*left_result) < dist(*right_result) else right_result
        result = min_pair(left_result + right_result)

        s_left = []
        left_coordinate = left - 1 if left >= 1 else 0
        for point in all_points[left_coordinate::-1]:
            if all_points[left][0] - point[0] <= dist(*result):
                s_left.append(point)
            else:
                break

        s_right = []
        for point in all_points[right+1:]:
            if point[0] - all_points[right][0] <= dist(*result):
                s_right.append(point)
            else:
                break

        s = sorted(s_left + s_right, key=lambda p : p[0])

        if len(s) >= 2:
            s_min = min_pair(s)
            print('-'*40)
            print_points(s)
            print(f"{s_min=}")
            print('-'*40)
            # result = result if dist(*result) < dist(*s_min) else s_min
            print(f"{result=}, {s=}")
            result = min_pair(list(result) + s)

    print(f"{result=}")

    return result
