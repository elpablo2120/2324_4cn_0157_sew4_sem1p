"""
__author__ = "Paul Waldecker"
__email__ = "0157@htl.rennweg.at"
__version__ = "0.1"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Ready to Review"
"""

import random

import miller_rabin
import math


def generate_prime(bit_length: int) -> int:
    """
    Generiert eine Primzahl mit der angegebenen Bit-Länge.
    :param bit_length: Länge der Primzahl in Bit
    :return: Primzahl
    >>> p = generate_prime(4)
    >>> isinstance(p, int)
    True
    >>> miller_rabin.is_prime(p)
    True
    >>> p.bit_length()
    4
    """
    p = 4
    while not miller_rabin.is_prime(p):
        p = random.getrandbits(bit_length)
        p |= (1 << bit_length - 1) | 1
    return p


def ggt(x: int, y: int) -> int:
    """
    Berechnet den größten gemeinsamen Teiler von x und y.
    :param x: Zahl 1
    :param y: Zahl 2
    :return: größter gemeinsamer Teiler der beiden Zahlen
    >>> ggt(12, 15)
    3
    >>> ggt(12, 0)
    12
    >>> ggt(0, 15)
    15
    """
    while y != 0:
        x, y = y, x % y
    return x


def generate_keys(number_of_bits):
    """
    Generiert einen privaten und einen öffentlichen Schlüssel für RSA.
    :param number_of_bits: Anzahl der Bits
    :return: Tuple mit privatem und öffentlichem Schlüssel und deren bit-Länge
    >>> (e, n, _), (d, _, _) = generate_keys(1024)
    >>> random_numbers = [random.getrandbits(1024) for _ in range(10)]
    >>> for x in random_numbers:
    ...    c = pow(x, e, n)
    ...    y = pow(c, d, n)
    ...    assert x == y
    """
    while True:
        p = generate_prime(math.ceil(number_of_bits / 2) + 1)
        q = generate_prime(number_of_bits // 2)
        n = p * q
        if n.bit_length() > number_of_bits:
            break

    phi_n = (p - 1) * (q - 1)
    e = random.getrandbits(number_of_bits)
    g = ggt(e, phi_n)
    while g != 1:
        e = random.getrandbits(number_of_bits)
        g = ggt(e, phi_n)

    d = pow(e, -1, phi_n)

    public_key = (e, n, e.bit_length())
    private_key = (d, n, d.bit_length())

    return (private_key, public_key)
