from collections import Counter

start = 0
end = 50
k = 2


def is_k_prime(n, k):
    if n < 2:
        return

    primes = []
    num = n

    i = start if start > 1 else 2

    while i <= end:
        if num % i == 0:
            primes.append(i)
            num /= i
        else:
            i += 1

    print(n, primes)


# is_k_prime(9, 2)


for i in range(start, end+1):
    is_k_prime(i, 2)
