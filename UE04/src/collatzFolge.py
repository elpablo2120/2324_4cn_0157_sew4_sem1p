from typing import List, Tuple


def collatz(n: int):
    """
        :param n: natürliche Zahl
        :return: wenn gerade Zahl n/2
        :return: wenn ungerade Zahl 3*n+1
        >>> collatz(10)
        5
        >>> collatz(5)
        16
    """
    if n % 2 == 0:
        return int(n / 2)

    if n % 2 != 0:
        return int(3 * n + 1)


def collatz_sequence(number: int) -> List[int]:
    """
    :param number: Startzahl
    :return: Collatz Zahlenfolge, resultierend aus n
    >>> collatz_sequence(19)
    [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    sequence = [number]
    while number != 1:
        number = collatz(number)
        sequence.append(number)

    return sequence


def longest_collatz_sequence(n: int) -> Tuple[int, int]:
    """
    :param n: Startzahl
    :return: Startwert und Länge der längsten Collatz Zahlenfolge deren Startwert <=n ist
    >>> longest_collatz_sequence(100)
    (97, 119)
    """
    max_length = 0
    start_number = 0
    for i in range(1, n + 1):
        collatz_list = collatz_sequence(i)
        current_length = len(collatz_list)
        if current_length > max_length:
            max_length = current_length
            start_number = i

    return start_number, max_length
