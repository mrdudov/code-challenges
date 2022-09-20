def dbl_linear(n):
    def get_y(x):
        return 2 * x + 1

    def get_z(x):
        return 3 * x + 1

    sequence = [1]

    # index = 0
    # while len(sequence) <= n:
    for index in range(n):
        next_y = get_y(sequence[index])
        next_z = get_z(sequence[index])
        sequence.extend([next_y, next_z])
        sequence = list(set(sequence))
        sequence.sort()
        # index += 1
    print(sequence)
    for index, value in enumerate(sequence):
        print(f"{index:3} - {value:3}")
    return sequence[n]
