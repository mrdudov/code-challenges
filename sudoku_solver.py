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
    BLOCK_SIZE = 3
    FIELD_SIZE = 9

    f_range = range(FIELD_SIZE)
    b_range = range(BLOCK_SIZE)
    d_set = set(range(1, FIELD_SIZE + 1))

    def print_p(p):
        print('-'*60)
        for i in f_range:
            print(p[i])

    def iter_puzzle():
        for i in f_range:
            for j in f_range:
                yield i, j

    def get_block_points(b_i, b_j):
        return [(b_i*BLOCK_SIZE + i, b_j*BLOCK_SIZE + j) for i in b_range for j in b_range]

    def iter_block():
        for b_i in b_range:
            for b_j in b_range:
                yield b_i, b_j
    
    def get_block_ij(i, j):
        return i // BLOCK_SIZE, j // BLOCK_SIZE

    def get_v_set(p, i):
        return set([p[k][i] for k in f_range if isinstance(p[k][i], int) and p[k][i] != 0])

    def get_h_set(p, i):
        return set([p[i][k] for k in f_range if isinstance(p[i][k], int) and p[i][k] != 0])

    def get_block_set(p, b_i, b_j):
        block_set = get_block_points(b_i, b_j)
        return set([p[i[0]][i[1]] for i in block_set if isinstance(p[i[0]][i[1]], int) and p[i[0]][i[1]] != 0])

    def get_posable_set(p, i, j):
        block_set = get_block_set(p, *get_block_ij(i,j))
        posable_set = d_set - (get_v_set(p, j) | get_h_set(p, i) | block_set)

        if len(posable_set) == 0:
            raise NoPosableValue

        return posable_set

    def is_solved(p):
        for i, j in iter_puzzle():
            if get_v_set(p, j) != d_set or get_h_set(p, i) != d_set:
                return False
        for b_i, b_j in iter_block():
            if get_block_set(p, b_i, b_j) != d_set:
                return False
        return True

    def iter_puzzle_set_val(p):
        for i, j in iter_puzzle():
            if isinstance(p[i][j], set):
                yield i, j, p[i][j]

    def calc_posable_set(p):
        for i, j in iter_puzzle():
            if p[i][j] not in d_set:
                p[i][j] = get_posable_set(p, i, j)
        return p

    def solver(p):
        if is_solved(p):
            return p
        try:
            i_min, j_min, p_set = min(
                iter_puzzle_set_val(p), key=lambda x: len(x[2]))
        except:
            print('shzhzghzfghzfghzfghzsfh')
            print_p(p)

        for val in p_set:
            new_p = deepcopy(p)
            new_p[i_min][j_min] = val
            try:
                new_p = calc_posable_set(new_p)
            except NoPosableValue:
                continue
            solution = solver(new_p)
            if is_solved(solution):
                return solution
        print_p(new_p)
        raise ValueError

    p = calc_posable_set(puzzle)
    p = solver(p)
    return p


if __name__ == '__main__':
    result = sudoku(puzzle)
