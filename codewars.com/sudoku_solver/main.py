from time import time

from algorithm import sudoku_solver
from src.functions import print_p
from tests.data_set import data_set


def main():
    start = time()
    result = sudoku_solver(data_set[0]["puzzle"])
    print(time() - start)
    print_p(result)


if __name__ == '__main__':
    main()
