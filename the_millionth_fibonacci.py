# https://www.codewars.com/kata/53d40c1e2f13e331fc000c26/train/python

import decimal
import numpy as np

def fib(n):


    decimal.getcontext().prec = 10000

    root_5 = decimal.Decimal(5).sqrt()
    phi = ((1 + root_5) / 2)

    a = (np.power(phi, n) - np.power(-phi, -n)) / root_5
#     if n > 1_000_000:
#         print(round(a))
    return round(a)

assert fib(0) == 0
assert fib(1) == 1
assert fib(2) == 1
assert fib(3) == 2
assert fib(4) == 3
assert fib(5) == 5
assert fib(-6) == -8
assert fib(-96) == -51680708854858323072
assert fib(-33) == 3524578
assert fib(-20) == -6765
assert fib(-37) == 24157817
assert fib(-89) == 1779979416004714189
assert fib(-86) == -420196140727489673
assert fib(-37) == 24157817
assert fib(-60) == -1548008755920
assert fib(-25) == 75025
assert fib(-97) == 83621143489848422977
assert fib(-18) == -2584

# assert fib(1000) == 4E208
# assert fib(1001) / fib(1000) == (1 + sqrt(5)) / 2
# assert fib(88119)
# assert fib(1405306)
