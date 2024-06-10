"""
__author__ = "Paul Waldecker"
__email__ = "0157@htl.rennweg.at"
__version__ = "0.1"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "In Progress"
"""

import random

FIRST_100_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                    31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
                    73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
                    127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
                    179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
                    233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
                    283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
                    353, 359, 367, 373, 379, 383, 389, 397, 401, 409,
                    419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
                    467, 479, 487, 491, 499, 503, 509, 521, 523, 541]


def is_prime(number):
    """
    Teste die ersten 100 Primzahlen auf Primzahl.
    """
    for prime in FIRST_100_PRIMES:
        if number % prime == 0:
            return number == prime

    return is_prim_millerrabin(number) == "probably prime"


def is_prim_millerrabin(number, iterations=20):
    """
    Teste die ersten 100 Primzahlen auf Primzahl mittels Miller-Rabin-Test. Mindestens 20 Iterationen.
    """
    if number % 2 == 0 or number < 2:
        return "composite"

    # number - 1 = odd_part*2^exponent - 1
    exponent, odd_part = 0, number - 1
    while odd_part % 2 == 0:
        odd_part //= 2
        exponent += 1

    def is_composite(base, odd_part, number, exponent):
        """
        Teste, ob die Zahl zusammengesetzt ist.

        :param base: Basis
        :param odd_part: ungerader Teil von number - 1
        :param number: Die zu testende Zahl
        :param exponent: Exponent der die Zahl in die Form number - 1 = odd_part*2^exponent - 1 bringt
        :return: True, wenn die Zahl zusammengesetzt ist, sonst False
        """
        base_power = pow(base, odd_part, number)
        if base_power in (1, number - 1):
            return False
        for _ in range(exponent - 1):
            base_power = pow(base_power, 2, number)
            if base_power == number - 1:
                return False
        return True

    for _ in range(iterations):
        base = random.randint(2, number - 2)
        if is_composite(base, odd_part, number, exponent):
            return "composite"

    return "probably prime"


def generate_prime(bit_length):
    """
    Generiere eine Primzahl mit einer bestimmten Bitlänge.
    """
    while True:
        prime_candidate = random.getrandbits(bit_length)
        # Setze das höchste und niedrigste Bit, um sicherzustellen, dass die Zahl die richtige Bitlänge hat und
        # ungerade ist
        prime_candidate |= (1 << (bit_length - 1)) | 1
        if is_prime(prime_candidate):
            return prime_candidate


if __name__ == '__main__':
    print("Teste Miller-Rabin-Algorithmus:")
    test_numbers = [221, 24566544301293569, 2512]
    for number in test_numbers:
        print(f"Die Zahl {number} ist {'eine Primzahl' if is_prime(number) else 'keine Primzahl'}")

    print("\nErste Primzahl mit mehr als 512 Bits:")
    number = pow(2, 512) + 1
    while not is_prime(number):
        number += 2
    print(number)

    print("\nVersteckte Nachricht in 24566544301293569 als Binärzahl mit 12 Zeichen/Zeile:")
    binary = bin(24566544301293569)[2:]
    for i in range(0, len(binary), 12):
        print(binary[i:i + 12])

    print("\nVersteckte Nachricht in 24566544301293569 als ASCII-Zeichen:")
    ascii = "".join([chr(int(binary[i:i + 8], 2)) for i in range(0, len(binary), 8)])
    print(ascii)

    print("\nNächst höhere Primzahl von 24566544301293569:")
    prime_higher = 24566544301293570
    while not is_prime(prime_higher):
        prime_higher += 1
    print(prime_higher)

    print("\nVersteckte Nachricht in nächst höhere Prim als Binärzahl mot 12 Zeichen/Zeile:")
    binary = bin(24566544301293587)[2:]
    for i in range(0, len(binary), 12):
        print(binary[i:i + 12])

    print("\nVersteckte Nachricht in nächst höhere Prim als ASCII-Zeichen:")
    ascii = "".join([chr(int(binary[i:i + 8], 2)) for i in range(0, len(binary), 8)])
    print(ascii)

    print("\nUnterschiede in den beiden binären Primzahlen (mit XOR ermittelt):")
    binary1 = bin(24566544301293569)[2:]
    binary2 = bin(24566544301293587)[2:]
    xor = "".join([str(int(binary1[i]) ^ int(binary2[i])) for i in range(len(binary1))])
    for i in range(0, len(xor), 12):
        print(xor[i:i + 12])