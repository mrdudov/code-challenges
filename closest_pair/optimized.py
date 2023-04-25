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
    
    print('-'*80)
    print(f"({left}, {right})") 
    print("")
    
    
    if data_set_len < 2:
        print(points)
        print(f"{left=}")
        print(f"{right=}")
        raise ValueError('points count less then two')
        
    
    if data_set_len == 2:
        result = points


    if data_set_len == 3:
        result = min_pair(points)
    
    if data_set_len > 3:

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
        
        result = left_result if dist(*left_result) < dist(*right_result) else right_result

        s_left = []
        for point in all_points[left::-1]:
            if dist(point, result[0]) < dist(*result):
                s_left.append(point)
            else:
                break

        s_right = []
        for point in all_points[right:]:
            if dist(point, result[0]) < dist(*result):
                s_right.append(point)
            else:
                break

        s = s_left + s_right

        if len(s) >= 2:
            s_min = min_pair(s)
            result = result if dist(*result) < dist(*s_min) else s_min

    return result
