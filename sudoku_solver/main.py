import test_data
from time import time

from sudoku_solver import  sudoku_solver
from tools import print_p


def main():
    start = time()
    result = sudoku_solver(test_data.test_puzzle)
    print(time() - start)
    print_p(result)


if __name__ == '__main__':
    main()
