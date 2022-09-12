import time


def kprimes_step(k, step, start, nd):

    sieve = list(range(nd + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(2*i, len(sieve), i):
                sieve[j] = 0
    lst = [i for i in sieve if i != 0]

    def is_k_prime(n, k):

        prime_iter = iter(lst)

        if n < 2 ^ k:
            return False

        primes = []
        num = n
        i = next(prime_iter)

        while i <= n // 2:
            if num % i == 0:
                primes.append(i)
                num /= i
                if len(primes) > k:
                    return False
            else:
                i = next(prime_iter)

        return True if len(primes) == k else False

    result = []

    i = start
    while i <= nd:
        if is_k_prime(i, k) and is_k_prime(i + step, k):
            result.append([i, i + step])
            i += step
        else:
            i += 1

    return result


start = time.time()
# print(kprimes_step(2, 10, 0, 50))
# print(kprimes_step(6, 14, 2113665, 2113889))
print(kprimes_step(6, 8, 2627371, 2627581))


print(time.time() - start)
