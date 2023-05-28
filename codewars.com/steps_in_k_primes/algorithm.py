from src.exceptions import KException
from src.functions import get_primes

def k_primes_step(k: int, step: int, start: int, nd: int):
    result = []

    primes = get_primes(nd=nd, k=k)

    i = start
    while i <= nd - step:
        max_divider_1 = i / 2 ** k
        max_divider_2 = i / 2 ** k
        dividers_count_1 = 0
        dividers_count_2 = 0
        num_1 = i
        num_2 = i + step
        primes_iter_1 = iter(primes)
        primes_iter_2 = iter(primes)
        j_1 = next(primes_iter_1)
        j_2 = next(primes_iter_2)
        try:
            while j_1 <= max_divider_1:
                while num_1 % j_1 == 0:
                    dividers_count_1 += 1
                    num_1 /= j_1
                    max_divider_1 = num_1
                    if dividers_count_1 > k:
                        raise KException
                try:
                    j_1 = next(primes_iter_1)
                except StopIteration:
                    break
            if dividers_count_1 != k:
                raise KException
            while j_2 <= max_divider_2:
                while num_2 % j_2 == 0:
                    dividers_count_2 += 1
                    num_2 /= j_2
                    max_divider_2 = num_2
                    if dividers_count_2 > k:
                        raise KException
                try:
                    j_2 = next(primes_iter_2)
                except StopIteration:
                    break
            if dividers_count_2 == k:
                result.append([i, i + step])

        except KException:
            pass
        i += 1
    return result
