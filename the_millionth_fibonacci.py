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
