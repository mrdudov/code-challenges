from time import time
from functools import reduce
from pprint import pprint


class k_exc(Exception):
    pass


def kprimes_step(k, step, start, nd):
    result = []

    primes = list(range(nd // 2 + 1))
    primes[1] = 0
    for i in primes:
        if i > 1:
            for j in range(2*i, len(primes), i):
                primes[j] = 0
    primes = [i for i in primes if i != 0]

    i = start
    while i <= nd - step:
        max_devider_1 = (i / 2) + 1
        max_devider_2 = (i / 2) + 1
        try:
            dividers_1, dividers_2 = [], []
            num_1, num_2 = i, i + step
            primes_irer_1 = iter(primes)
            primes_irer_2 = iter(primes)
            j = next(primes_irer_1)
            l = next(primes_irer_2)
            while j <= max_devider_1:
                while num_1 % j == 0:
                    dividers_1.append(j)
                    num_1 /= j
                    max_devider_1 = num_1
                    if len(dividers_1) > k:
                        raise k_exc
                try:
                    j = next(primes_irer_1)
                except StopIteration:
                    break
            if len(dividers_1) != k:
                raise k_exc
            while l <= max_devider_2:
                while num_2 % l == 0:
                    dividers_2.append(l)
                    num_2 /= l
                    max_devider_2 = num_2
                    if len(dividers_2) > k:
                        raise k_exc
                try:
                    l = next(primes_irer_2)
                except StopIteration:
                    break

            if len(dividers_2) == k:
                result.append([i, i + step])
            i += 1

        except k_exc:
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
]

start = time()

for i, arg in enumerate(args):
    local_start = time()
    res = kprimes_step(*arg[0])
    # print(arg[0])
    print(
        f"{i+1} {res == arg[1]} {len(res), len(arg[1])} time: {time()-local_start:.3f}")

    # print(len(res), len(arg[1]))

    # for p in range(max(len(res), len(arg[1]))):
    #     print(f"{res[p]} {arg[1][p]} - {res[p] == arg[1][p]}")


print(f'total time: {time() - start:.3f}')
