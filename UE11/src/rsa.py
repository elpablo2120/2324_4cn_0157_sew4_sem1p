"""
__author__ = "Paul Waldecker"
__email__ = "0157@htl.rennweg.at"
__version__ = "0.1"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "In Progress"
"""

# Keys erzeugen generate_keys(number_of_bits)
# Datei: rsa.py
# Parameter: gewünschte Länge des Keys in bits bzw. welche Blockgröße soll beim Verschlüsseln verwendet werden8.
# 7Zwischenergebnis speichern! nicht zwei rekursive Ausfrufe mit dem selben Wert
# 8da ist ein kleiner Unterschied, wir nehmen die zweite Definition
# Vorgehen:
# • zwei Primzahlen p, q erzeugen, etwa mit der halben Anzahl an Bits9
# – die halbe Anzahl ist natürlich eine Einschränkung, andererseits gibt es10 ca. 2 ⋅ 10151 Primzahlen mit einer
# Länge von 512 Bit.
# • bestimme n = p*q
# – n muss mehr als die erforderliche Anzahl an Bits haben!11
# – Kontrolle: n.bit_length() > Blockgröße
# • bestimme e: große Zufallszahl. Diese muss teilerfremd zu 𝜑(𝑛) = (𝑝 − 1) ⋅ (𝑞 − 1) sein12!
# • bestimme d = ModInverse(e, (p-1)*(q-1)) = die multiplikativ Inverse zu 𝑒 mod 𝜑(𝑛).
# – Es muss daher folgende Gleichung gelten: 𝑒 ⋅ 𝑑 = 1 mod 𝜑(𝑛).
# – Tipp: Dokumentation zu pow()13 oder Extended Euclidean algorithm bzw. fast mod inverse
# • Ergebnis ist ein Tupel: (private key, public key)
# – jeder Key besteht aus ( e bzw. d, n, keylen)14
# Ultimativer Test – als doctest:
# for x in [ ...a lot of numbers, small and large...]:
# c = pow(x, e, n)
# y = pow(c, d, n)
# assert x == y

import random
import miller_rabin


def generate_prime(bit_length):
    p = 4
    # Keep generating until a prime is found
    while not miller_rabin.is_prime(p):
        # Generate random bits
        p = random.getrandbits(bit_length)
        # Apply a mask to set MSB and LSB to 1 to ensure prime candidate is of correct bit length
        p |= (1 << bit_length - 1) | 1
    return p


def ggt(x: int, y: int) -> int:
    while y != 0:
        x, y = y, x % y
    return x


def generate_keys(number_of_bits):
    n = 0
    while n.bit_length() <= number_of_bits:
        p = generate_prime((number_of_bits // 2) + 1)
        q = generate_prime(number_of_bits // 2)
        n = p * q

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


print(generate_keys(4))
