import decimal
import numpy as np
import gmpy2

def fib(n):
    if n < 0:
        decimal.getcontext().prec = 25_000
        root_5 = decimal.Decimal(5).sqrt()
        phi = ((1 + root_5) / 2)
        a = (np.power(phi, n) - np.power(-phi, -n)) / root_5
        return round(a)
    return gmpy2.fib(n)
