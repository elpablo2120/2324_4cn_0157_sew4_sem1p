def M(n: int) -> int:
    """
    Diese Funktion führt eine rekursive Berechnung durch, basierend auf einer gegebenen Eingabezahl.

    :param n: Eingabezahl
    :return: Ergebnis der rekursiven Berechnung.

    >>> M(100)
    91
    >>> M(120)
    110
    """
    if n <= 100:
        return M(M(n + 11))
    if n > 100:
        return n - 10


if __name__ == "__main__":
    from time import time

    t0 = time()

    m_list = [M(n) for n in range(2000)]
    print(m_list)

    m_dict = {n: M(n) for n in range(2000)}
    print(m_dict)

    elapsed_time = time() - t0
    print(f"Die Berechnung dauerte {elapsed_time:} Sekunden.")
