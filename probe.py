import time


class k_exc(Exception):
    pass


def kprimes_step(k, step, start, nd):
    result = []

    sieve = list(range(nd // 2 + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(2*i, len(sieve), i):
                sieve[j] = 0
    lst = [i for i in sieve if i != 0]
    print(len(lst))

    i = start
    while i <= nd - step:
        try:
            primes_1, primes_2 = [], []
            num_1, num_2 = i, i + step
            for j in lst:
                while num_1 % j == 0:
                    primes_1.append(j)
                    num_1 /= j
                    if len(primes_1) > k:
                        raise k_exc
            if len(primes_1) == k:
                for l in lst:
                    while num_2 % l == 0:
                        primes_2.append(l)
                        num_2 /= l
                        if len(primes_2) > k:
                            raise k_exc
            else:
                raise k_exc
            if len(primes_2) == k:
                result.append([i, i + step])
                i += step
            else:
                i += 1
        except k_exc:
            i += 1
    return result


args = [
    ((2, 10, 0, 50), [[4, 14], [15, 25], [25, 35], [39, 49]]),
    ((6, 14, 2113665, 2113889), [[2113722, 2113736]]),
    ((10, 8, 2425364, 2425700), []),
    ((6, 8, 2627371, 2627581), [[2627408, 2627416],
     [2627440, 2627448], [2627496, 2627504]])
]

start = time.time()

for arg in args:
    res = kprimes_step(*arg[0])
    print(f"{res == arg[1]} kprimes_step{arg[0]}={res}")

print(time.time() - start)
