def M(n):
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

    m_list = [M(n) for n in range(200)]
    print(m_list)

    m_dict = {n: M(n) for n in range(200)}
    print(m_dict)

    # Was ist bemerkenswert beim Ergebnis dieser Funktion?
    # Antwort: Die Funktion hat eine selbstreferenzielle Struktur (rekursive Definition) und kann zu komplexen Werten führen.

    t0 = time()

    elapsed_time = time() - t0
    print(f"Die Berechnung dauerte {elapsed_time:.6f} Sekunden.")
