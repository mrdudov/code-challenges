from time import time
from itertools import zip_longest


class k_exc(Exception):
    pass


def kprimes_step(k, step, start, nd):
    result = []

    primes = list(range(nd // 2**(k-2)))
    primes[1] = 0
    for p in primes:
        if p > 1:
            for j in range(2*p, len(primes), p):
                primes[j] = 0
    primes = [p for p in primes if p != 0]

    i = start
    while i <= nd - step + 1:
        max_devider_1 = i / 2 ** k + 1
        max_devider_2 = i / 2 ** k + 1
        dividers_count_1 = 0
        dividers_count_2 = 0
        num_1 = i
        num_2 = i + step
        primes_iter_1 = iter(primes)
        primes_iter_2 = iter(primes)
        j_1 = next(primes_iter_1)
        j_2 = next(primes_iter_2)
        try:
            while j_1 <= max_devider_1:
                while num_1 % j_1 == 0:
                    dividers_count_1 += 1
                    num_1 /= j_1
                    max_devider_1 = num_1
                    if dividers_count_1 > k:
                        raise k_exc
                try:
                    j_1 = next(primes_iter_1)
                except StopIteration:
                    break
            if dividers_count_1 != k:
                raise k_exc
            while j_2 <= max_devider_2:

                while num_2 % j_2 == 0:
                    firsr_dv = j_2
                    dividers_count_2 += 1
                    num_2 /= j_2
                    max_devider_2 = num_2
                    if dividers_count_2 > k:
                        raise k_exc
                try:
                    j_2 = next(primes_iter_2)
                except StopIteration:
                    break
            if dividers_count_2 == k:
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
    ((2, 5, 291583, 291934), [[291638, 291643],
                              [291758, 291763],
                              [291794, 291799],
                              [291806, 291811],
                              [291866, 291871],
                              [291898, 291903],
                              [291926, 291931],
                              [291929, 291934]]),
]


start = time()

for i, arg in enumerate(args):
    local_start = time()
    res = kprimes_step(*arg[0])
    # print(arg[0])
    print(
        f"{i+1} {res == arg[1]} {len(res), len(arg[1])} time: {time()-local_start:.3f}")

    # print(f"{len(res)=}, {len(arg[1])=}")

    # for p in zip_longest(res, arg[1]):
    #     print(p)
    # print(f"{res[p]} {arg[1][p]} - {res[p] == arg[1][p]}")


print(f'total time: {time() - start:.3f}')
