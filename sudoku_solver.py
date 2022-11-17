from copy import deepcopy

puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]


solution = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]]


class NoPosableValue(Exception):
    pass


def sudoku(puzzle):
    r0_8 = range(9)
    r0_2 = range(3)
    s1_9 = set(range(1, 10))

    def print_p(p):
        print('-'*60)
        for i in r0_8:
            print(p[i])

    def iter_puzzle():
        for i in r0_8:
            for j in r0_8:
                yield i, j

    def iter_block():
        for b_i in r0_2:
            for b_j in r0_2:
                yield [(b_i*3 + i, b_j*3 + j) for i in r0_2 for j in r0_2]

    def get_v_set(p, i):
        return set([p[k][i] for k in r0_8 if isinstance(p[k][i], int) and p[k][i] != 0])

    def get_h_set(p, i):
        return set([p[i][k] for k in r0_8 if isinstance(p[i][k], int) and p[i][k] != 0])

    def get_block_set(p, b_i, b_j):
        pass

    def get_posable_set(p, i, j):
        posable_set = s1_9 - (get_v_set(p, j) | get_h_set(p, i))

        if len(posable_set) == 0:
            print("NoPosableValue")
            print(f'{get_v_set(p, j)=} {get_h_set(p, i)=}')
            print(f'{get_v_set(p, j) | get_h_set(p, i)=}')
            print_p(p)
            print(f'{i=}')
            print(f'{j=}')
            print("NoPosableValue")
            raise NoPosableValue

        if 0 in posable_set:
            print("ZERO IN POSABLE SET")
            print(f'{get_v_set(p, j)=} {get_h_set(p, i)=}')
            print_p(p)
            print(f'{i=}')
            print(f'{j=}')
            print("ZERO IN POSABLE SET")
            raise ValueError

        return posable_set

    def is_solved(p):
        for i, j in iter_puzzle():
            if get_v_set(p, j) != s1_9 or get_h_set(p, i) != s1_9:
                return False
        return True

    def iter_puzzle_set_val(p):
        for i, j in iter_puzzle():
            if isinstance(p[i][j], set):
                yield i, j, p[i][j]

    def calc_posable_set(p):
        for i, j in iter_puzzle():
            if p[i][j] not in s1_9:
                p[i][j] = get_posable_set(p, i, j)
        return p

    def solver(p):
        if is_solved(p):
            return p
        try:
            i_min, j_min, p_set = min(
                iter_puzzle_set_val(p), key=lambda x: len(x[2]))
        except:
            print('123454553tfghatehashzhzghzfghzfghzfghzsfh')
            print_p(p)

        for val in p_set:
            new_p = deepcopy(p)
            new_p[i_min][j_min] = val
            try:
                new_p = calc_posable_set(new_p)
            except NoPosableValue:
                continue
            solver(new_p)

        print_p(new_p)
        raise ValueError

    for c in iter_block():
        print(c)
        print('+'*60)

    print_p(puzzle)
    p = calc_posable_set(puzzle)
    print_p(p)
    p = solver(p)

    return p


if __name__ == '__main__':
    result = sudoku(puzzle)
