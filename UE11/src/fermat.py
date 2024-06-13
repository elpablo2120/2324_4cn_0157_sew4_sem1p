"""
__author__ = "Paul Waldecker"
__email__ = "0157@htl.rennweg.at"
__version__ = "0.1"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Ready to Review"
"""

from collections import Counter


def fermat(p):
    """
    Kleinster Satz von Fermat: a^(p-1) mod p = 1 für a = 1...p-1
    :param p: Primzahl
    :return: Liste von Werten
    >>> fermat(7)
    [1, 1, 1, 1, 1, 1]
    >>> fermat(11)
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    >>> fermat(13)
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    >>> fermat(8)
    [1, 0, 3, 0, 5, 0, 7]
    """
    return [pow(a, p - 1, p) for a in range(1, p)]


def display(values, p):
    """
    Anzeige der Ergebnisse für die Primzahl p in Prozent und Anzahl der Ergebnisse.
    :param values: Liste von Werten fermat(p)
    :param p: Primzahl
    >>> display([1, 1, 1, 1, 1, 1], 7)
    7 -> 100.00 % -> res[1]=6, len(res)=6 - [(1, 6)]
    >>> display([1, 0, 3, 0, 5, 0, 7], 8)
    8 -> 14.29 % -> res[1]=1, len(res)=7 - [(1, 1), (0, 3), (3, 1), (5, 1), (7, 1)]
    """
    counter = Counter(values)
    total = len(values)
    percentage = (counter[1] / total) * 100 if 1 in counter else 0
    print(f"{p} -> {percentage:.2f} % -> res[1]={counter[1]},"
          f" len(res)={total} - {list(counter.items())}")


if __name__ == '__main__':
    primes = list(range(2, 12)) + [997]
    non_primes = [9, 15, 21, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562,
                  563, 564, 565, 566, 567, 568, 569, 6601, 8911]

    print("Ergebnisse für Primzahlen von 2 bis 11 und 997:")
    for p in primes:
        display(fermat(p), p)

    print("\nErgebnisse für Nicht-Primzahlen:")
    for p in non_primes:
        display(fermat(p), p)
