from time import time
from functools import reduce
from pprint import pprint
from typing import List


class k_exc(Exception):
    pass


def kprimes_step(k, step, start, nd):
    result = []

    primes = list(range(nd // k))
    primes[1] = 0
    for p in primes:
        if p > 1:
            for j in range(2*p, len(primes), p):
                primes[j] = 0
    primes = [p for p in primes if p != 0]

    i = start
    while i <= nd - step:
        max_devider_1 = (i / 2) + 1
        max_devider_2 = (i / 2) + 1
        dividers_count_1 = []
        dividers_count_2 = []
        num_1 = i
        num_2 = i + step
        primes_iter_1 = iter(primes)
        primes_iter_2 = iter(primes)
        j = next(primes_iter_1)
        l = next(primes_iter_2)
        try:
            while j <= max_devider_1:
                while num_1 % j == 0:
                    dividers_count_1.append(j)
                    num_1 /= j
                    max_devider_1 = num_1
                    if len(dividers_count_1) > k:
                        raise k_exc
                try:
                    j = next(primes_iter_1)
                except StopIteration:
                    break
            if len(dividers_count_1) != k:
                raise k_exc
            while l <= max_devider_2:
                while num_2 % l == 0:
                    dividers_count_2.append(l)
                    num_2 /= l
                    max_devider_2 = num_2
                    if len(dividers_count_2) > k:
                        raise k_exc
                try:
                    l = next(primes_iter_2)
                except StopIteration:
                    break
            if len(dividers_count_2) == k:
                result.append([i, i + step])

        except k_exc:
            pass
        i += 1
    return result


args = [
    ((10, 8, 2425364, 2425700), []),
    ((6, 8, 2627371, 2627581), [[2627408, 2627416],
                                [2627440, 2627448],
                                [2627496, 2627504]]),
    ((6, 8, 2627408, 2627504), [[2627408, 2627416],
                                [2627440, 2627448],
                                [2627496, 2627504]]),
    ((5, 11, 2986889, 2987279), [[2987037, 2987048],
                                 [2987050, 2987061],
                                 [2987176, 2987187]]),
    ((6, 14, 2113665, 2113889), [[2113722, 2113736]]),
    ((2, 7, 217565, 217796), [[217582, 217589],
                              [217599, 217606],
                              [217642, 217649],
                              [217731, 217738],
                              [217762, 217769]
                              ]),
]


start = time()

for i, arg in enumerate(args):
    local_start = time()
    res = kprimes_step(*arg[0])
    # print(arg[0])
    print(
        f"{i+1} {res == arg[1]} {len(res), len(arg[1])} time: {time()-local_start:.3f}")

    # print(f"{len(res)=}, {len(arg[1])=}")

    # for p in range(max(len(res), len(arg[1]))):
    #     print(f"{res[p]} {arg[1][p]} - {res[p] == arg[1][p]}")


print(f'total time: {time() - start:.3f}')
