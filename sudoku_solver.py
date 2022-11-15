from pprint import pprint


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


def sudoku(puzzle):
    r0_8 = range(9)
    s1_9 = set(range(1, 10))

    def get_v_set(p, i):
        return set([p[i][k] for k in r0_8 if isinstance(p[i][k], int)])

    def get_h_set(p, i):
        return set([p[k][i] for k in r0_8 if isinstance(p[k][i], int)])

    def get_hv_set(p, i, j):
        return (get_v_set(p, j) | get_h_set(p, i)) ^ (s1_9 | {0})

    def is_solved(p):
        for i in r0_8:
            if get_v_set(p, i) != s1_9 or get_v_set(p, i) != s1_9:
                return False
        return True

    def solver(p):
        pass

    for i, line in enumerate(puzzle):
        for j, val in enumerate(line):
            if val not in s1_9:
                puzzle[i][j] = get_hv_set(p=puzzle, i=i, j=j)

    solver(puzzle)
    is_solved(puzzle)

    print('-'*60)
    for i in r0_8:
        print(puzzle[i])

    return puzzle


if __name__ == '__main__':
    result = sudoku(puzzle)
