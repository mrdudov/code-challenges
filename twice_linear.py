from time import time
import math


def dbl_linear(n):

    sequence = [1]
    res = [1]
    c = math.ceil(math.log(n+1, 2))
    for _ in range(c+2):
        sequence_y = [2 * x + 1 for x in sequence]
        sequence_z = [3 * x + 1 for x in sequence]
        sequence = sequence_y + sequence_z
        res.extend(sequence)
    res = sorted(list(set(res)))
    return res[n]


data = [
    (10, 22),
    (20, 57),
    (30, 91),
    (50, 175),
    (100, 447),
    (500, 3355),
    (1000, 8488),
    (2000, 19773),
    (6000, 80914),
    (60000, 1511311),
]

t_start = time()

for i, val in enumerate(data):
    t_local = time()
    res = dbl_linear(val[0])
    print(
        f"{i+1} {res == val[1]} t={time()-t_local:.3f} n={val[0]} f(n)={res}")

print(f"total time: {time() - t_start:.3f}")
