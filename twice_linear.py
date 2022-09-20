from time import time
import math


def dbl_linear(n):
    
    def get_y_z(x):
        return 2 * x + 1, 3 * x + 1

    sequence = [1]

    for index in range(n):
        sequence.extend(get_y_z(sequence[index]))
        sequence = list(set(sequence))
        sequence.sort()
        # if len(sequence) > n:
        #     print(sequence)
        #     break
    # print(f"{n=} {len(sequence)=}")
    return sequence[n]

n = 6000

data = [
    (10, 22),
    (20, 57),
    (30, 91),
    (50, 175),
    (100, 447),
    (500, 3355),
    (1000, 8488),
    (2000, 19773),
    # (6000, 80914),
    # (60000, 1511311),
]

t_start = time()

for i, val in enumerate(data):
    t_local = time()
    res = dbl_linear(val[0])
    print(f"{i+1} {res == val[1]} t={time()-t_local:.3f} n={val[0]} f(n)={res}")

print(f"total time: {time() - t_start:.3f}")
