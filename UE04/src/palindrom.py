import string


def is_palindrom(s: str):
    return s == s[::-1]


def is_palindrom_sentence(s: str):
    translator = str.maketrans("", "", string.punctuation)
    result = s.translate(translator).replace(" ", "").lower()
    return result == result[::-1]


def palindrom_produkt(x):
    n = 0
    for i in range(x, 0, -1):
        for j in range(i, 0, -1):
            x = i * j
            if x > n:
                if is_palindrom(str(x)):
                    n = x
    return n


def get_dec_hex_palindrom(x):
    n = 0
    for i in range(x, 0, -1):
        if is_palindrom(str(i)) and is_palindrom(to_base(i, 16)):
            n = i
            break
    return n, to_base(n, 16)


def to_base(number: int, base: int) -> str:
    """
    :param number: Zahl im 10er-Syste,
    :param base: Zielsystem
    :return: Zahl im Zielsystem als String
    >>> to_base(1234,16)
    '4D2'
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


print(is_palindrom("ohcelloollecho"))
print(is_palindrom("9009"))
print(is_palindrom_sentence("Oh, Cello! oll Echo!"))
print(palindrom_produkt(99))
print(to_base(1234, 16))
print(get_dec_hex_palindrom(1000))
