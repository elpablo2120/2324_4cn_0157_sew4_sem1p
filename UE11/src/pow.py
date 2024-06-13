"""
__author__ = "Paul Waldecker"
__email__ = "0157@htl.rennweg.at"
__version__ = "0.1"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Ready to Review"
"""
import time


def pow_iterativ(a, b, n):
    """
    Iterative version of pow
    :param a: base
    :param b: exponent
    :param n: modulo
    :return: a^b mod n
    >>> pow(63, 17, 91)
    7
    >>> pow_iterativ(63, 17, 91)
    7
    """
    result = 1
    while b > 0:
        if b % 2 == 1:
            result = result * a % n
        a = a * a % n
        b = b // 2
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    a = 829287393
    b = 34938439489348938493489348939201
    n = 927492839293

    start_time = time.time()
    print(pow_iterativ(a, b, n))
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time pow_iterativ:", execution_time * 1000, "ms")

    start_time = time.time()
    print(pow(a, b, n))
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time pow:", execution_time * 1000, "ms")
