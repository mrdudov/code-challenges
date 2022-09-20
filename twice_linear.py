from time import time

def dbl_linear(n):
    def get_y(x):
        return 2 * x + 1

    def get_z(x):
        return 3 * x + 1

    sequence = [1]

    for index in range(n):
        next_y = get_y(sequence[index])
        next_z = get_z(sequence[index])
        sequence.extend([next_y, next_z])
        sequence = list(set(sequence))
        sequence.sort()

    return sequence[n]


n = 6000

t_start = time()

res = dbl_linear(n)
print(f"{n=} f(n)={res}")

print(time() - t_start)
