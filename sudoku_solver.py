from copy import deepcopy
from time import time


class NoPosableValue(Exception):
    pass


class NoSolution(Exception):
    pass


def print_p(p):
    print('-'*60)
    for line in p:
        print(line)


def sudoku(puzzle):
    BLOCK_SIZE = 3
    FIELD_SIZE = 9

    f_range = range(FIELD_SIZE)
    b_range = range(BLOCK_SIZE)
    d_set = set(range(1, FIELD_SIZE + 1))

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

    def get_v_points(i):
        return [(k, i) for k in f_range]

    def get_h_points(i):
        return [(i, k) for k in f_range]

    def get_v_set(p, i):
        return {x for k in f_range if isinstance((x := p[k][i]), int) and x != 0}

    def get_h_set(p, i):
        return {x for k in f_range if isinstance((x := p[i][k]), int) and x != 0}

    def get_block_set(p, b_i, b_j):
        block_set = get_block_points(b_i, b_j)
        return {x for i in block_set if isinstance((x := p[i[0]][i[1]]), int) and x != 0}

    def get_posable_set(p, i, j):
        block_set = get_block_set(p, *get_block_ij(i, j))
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

    def remove_val_from_posable_set(p, i, j, val):
        h_points = get_h_points(i)
        v_points = get_v_points(j)
        block_points = get_block_points(*get_block_ij(i, j))
        points = set(h_points + v_points + block_points)
        for p_i, p_j in points:
            if isinstance(p[p_i][p_j], set):
                if len(p[p_i][p_j] - {val}) == 0:
                    raise NoPosableValue
                p[p_i][p_j] = p[p_i][p_j] - {val}
        return p

    def solver(p):
        if is_solved(p):
            return p
        try:
            i_min, j_min, p_set = min(
                iter_puzzle_set_val(p), key=lambda x: len(x[2]))
        except:
            raise NoSolution

        for val in p_set:
            new_p = deepcopy(p)
            new_p[i_min][j_min] = val
            try:
                new_p = remove_val_from_posable_set(new_p, i_min, j_min, val)
            except NoPosableValue:
                continue
            try:
                solution = solver(new_p)
            except NoSolution:
                continue
            if is_solved(solution):
                return solution
        raise NoSolution

    p = calc_posable_set(puzzle)
    p = solver(p)

    return p


if __name__ == '__main__':
    puzzle = [[9, 0, 0, 0, 8, 0, 0, 0, 1],
              [0, 0, 0, 4, 0, 6, 0, 0, 0],
              [0, 0, 5, 0, 7, 0, 3, 0, 0],
              [0, 6, 0, 0, 0, 0, 0, 4, 0],
              [4, 0, 1, 0, 6, 0, 5, 0, 8],
              [0, 9, 0, 0, 0, 0, 0, 2, 0],
              [0, 0, 7, 0, 3, 0, 2, 0, 0],
              [0, 0, 0, 7, 0, 5, 0, 0, 0],
              [1, 0, 0, 0, 4, 0, 0, 0, 7]]

    solution = [[9, 2, 6, 5, 8, 3, 4, 7, 1],
                [7, 1, 3, 4, 2, 6, 9, 8, 5],
                [8, 4, 5, 9, 7, 1, 3, 6, 2],
                [3, 6, 2, 8, 5, 7, 1, 4, 9],
                [4, 7, 1, 2, 6, 9, 5, 3, 8],
                [5, 9, 8, 3, 1, 4, 7, 2, 6],
                [6, 5, 7, 1, 3, 8, 2, 9, 4],
                [2, 8, 4, 7, 9, 5, 6, 1, 3],
                [1, 3, 9, 6, 4, 2, 8, 5, 7]]
    start = time()
    result = sudoku(puzzle)
    print(time() - start)
    print_p(result)
