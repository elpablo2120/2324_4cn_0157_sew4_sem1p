from typing import List, Tuple


def collatz(n: int, p: int = 3) -> int:
    """
    Berechnet den Collatz-Wert für eine gegebene natürliche Zahl.

    :param n: Natürliche Zahl
    :param p: Optionaler Parameter (Default-Wert: 3)
    :return: Wenn die Zahl gerade ist, wird n/2 zurückgegeben.
    :return: Wenn die Zahl ungerade ist, wird p*n+1 zurückgegeben.

    >>> collatz(10)
    5
    >>> collatz(5)
    16
    """
    if n % 2 == 0:
        return n // 2
    else:
        return p * n + 1


def collatz_sequence(number: int, p: int = 3) -> List[int]:
    """
    Erstellt die Collatz-Zahlenfolge, die von einer gegebenen Startzahl resultiert.

    :param number: Startzahl
    :param p: Optionaler Parameter (Default-Wert: 3)
    :return: Collatz-Zahlenfolge, die aus n resultiert.

    >>> collatz_sequence(19)
    [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    sequence = [number]
    while number != 1:
        number = collatz(number, p)
        sequence.append(number)

    return sequence


def longest_collatz_sequence(n: int, p: int = 3) -> Tuple[int, int]:
    """
    Findet den Startwert und die Länge der längsten Collatz-Zahlenfolge, deren Startwert <= n ist.

    :param n: Startzahl
    :param p: Optionaler Parameter (Default-Wert: 3)
    :return: Tuple mit dem Startwert und der Länge der längsten Collatz-Zahlenfolge.

    >>> longest_collatz_sequence(100)
    (97, 119)
    """
    max_length = 0
    start_number = 0
    for i in range(1, n + 1):
        collatz_list = collatz_sequence(i, p)
        current_length = len(collatz_list)
        if current_length > max_length:
            max_length = current_length
            start_number = i

    return start_number, max_length

print(longest_collatz_sequence(20000))