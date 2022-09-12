from collections import Counter
from typing import List


global_primes = set()


def get_all_primes(mux_nun: int) -> List[int]:
    primes = set()
    num = mux_nun
    i = 2

    while i <= mux_nun // 2 + 1:
        if num % i == 0:
            primes.add(i)
            num /= i
        else:
            i += 1

    return list(primes)


def is_k_prime(n, k):
    
    if n < 2^k:
        return False

    primes = []
    num = n
    i = 2
    c = Counter()

    while i <= n // 2 + 1:
        if num % i == 0:
            primes.append(i)
            num /= i
        else:
            i += 1
        c = Counter(primes)
        if c.total() > k:
            return False
    print(primes)
    if c.total() == k:
        return True
    
    return False


def kprimes_step(k, step, start, nd):
    
    k_prime_list = []
    result = []

    for i in range(start, nd+1):
        if is_k_prime(i, k):
            k_prime_list.append(i)
    print(k_prime_list)
    
    for i_count, i in enumerate(k_prime_list):
        for j in k_prime_list[i_count:]:
            if i + step == j:
                result.append([i, j]) 
    
    return result


if __name__ == '__main__1':
    result = kprimes_step(6, 14, 2113665, 2113889)
    print(result)


print(get_all_primes(2113884))
