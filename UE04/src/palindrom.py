import string

def is_palindrom(s: str) -> bool:
    """
    Überprüft, ob s ein Palindrom ist

    :param s: Eingabestring
    :return: True, wenn es sich um ein Palindrom handelt, False sonst

    >>> is_palindrom("ohcelloollecho")
    True
    >>> is_palindrom("9009")
    True
    >>> is_palindrom("hello")
    False
    """
    return s == s[::-1]


def is_palindrom_sentence(s: str) -> bool:
    """
    Überprüft, ob es sich um einen Palindromsatz handelt. Sonderzeichen und Leerzeichen werden entfernt.

    :param s: Eingabesatz
    :return: True, wenn es sich um einen Palindromsatz handelt, False sonst

    >>> is_palindrom_sentence("Oh, Cello! oll Echo!")
    True
    >>> is_palindrom_sentence("A man, a plan, a canal, Panama!")
    True
    >>> is_palindrom_sentence("Hello, world!")
    False
    """
    translator = str.maketrans("", "", string.punctuation)
    result = s.translate(translator).replace(" ", "").lower()
    return result == result[::-1]


def palindrom_produkt(x: int) -> int:
    """
    Findet das größte Palindrom, das das Produkt von zwei Zahlen kleiner oder gleich x ist.

    :param x: Obergrenze für die Zahlen
    :return: Größtes Palindromprodukt

    >>> palindrom_produkt(99)
    9009
    >>> palindrom_produkt(100)
    9009
    >>> palindrom_produkt(50)
    2112
    """
    n = 0
    for i in range(x, 0, -1):
        for j in range(i, 0, -1):
            product = i * j
            if product > n and is_palindrom(str(product)):
                n = product
    return n


def get_dec_hex_palindrom(x: int) -> tuple:
    """
    Findet die größte Dezimalzahl kleiner oder gleich x, die sowohl in dezimaler als auch in hexadezimaler Form ein Palindrom ist.

    :param x: Obergrenze für die Dezimalzahlen
    :return: Tuple mit dem dezimalen Palindrom und seiner hexadezimalen Darstellung

    >>> get_dec_hex_palindrom(1000)
    (979, '3D3')
    >>> get_dec_hex_palindrom(500)
    (353, '161')
    >>> get_dec_hex_palindrom(200)
    (11, 'B')
    """
    n = 0
    for i in range(x, 0, -1):
        if is_palindrom(str(i)) and is_palindrom(to_base(i, 16)):
            n = i
            break
    return n, to_base(n, 16)


def to_base(number: int, base: int) -> str:
    """
    Konvertiert eine Zahl von Dezimal in eine andere Basis.

    :param number: Zahl in Dezimalform
    :param base: Zielbasis
    :return: Zahl in der Zielbasis als Zeichenkette

    >>> to_base(1234, 16)
    '4D2'
    >>> to_base(255, 2)
    '11111111'
    >>> to_base(16, 8)
    '20'
    """
    digs = string.digits + string.ascii_uppercase

    if number < 0:
        sign = -1
    elif number == 0:
        return digs[0]
    else:
        sign = 1

    number *= sign
    digits = []

    while number:
        digits.append(digs[number % base])
        number = number // base

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)


# Beispielaufrufe
print(is_palindrom("ohcelloollecho"))
print(is_palindrom("9009"))
print(is_palindrom_sentence("Oh, Cello! oll Echo!"))
print(palindrom_produkt(99))
print(to_base(1234, 16))
print(get_dec_hex_palindrom(1000))
