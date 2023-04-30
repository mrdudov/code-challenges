class k_exc(Exception):
    pass


def kprimes_step(k: int, step: int, start: int, nd: int):
    result = []

    n = (nd // 2**(k-2))
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((n-i*i-1)//(2*i)+1)
    primes = tuple([2] + [i for i in range(3, n, 2) if sieve[i]])

    i = start
    while i <= nd - step:
        max_devider_1 = i / 2 ** k
        max_devider_2 = i / 2 ** k
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
