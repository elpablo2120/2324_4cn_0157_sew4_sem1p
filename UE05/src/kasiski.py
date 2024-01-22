"""
__author__ = "Paul Waldecker"
__email__ = "0157@htl.rennweg.at"
__version__ = "1.0.0"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Development"
"""


def encrypt(plaintext: str, key=None) -> str:
    ciphertext = ""
    for i in plaintext:
        ciphertext += chr((ord(i) - ord('a') + key) % 26 + ord('a'))
    return ciphertext


def decrypt(plaintext: str, key=None) -> str:
    ciphertext = ""
    for i in plaintext:
        ciphertext += chr((ord(i) - ord('a') - key) % 26 + ord('a'))
    return ciphertext


def crack(plaintext: str, elements=1) -> list[str]:
    # Deutsch Häufigkeitsanalyse (source: https://en.wikipedia.org/wiki/Letter_frequency)
    german_frequencies = {'e': 17.4, 'n': 9.8, 'i': 7.6, 's': 7.3, 'r': 7.0,
                          'a': 6.2, 't': 6.1, 'd': 5.5, 'h': 5.1, 'u': 4.2,
                          'l': 3.4, 'c': 3.0, 'g': 3.0, 'm': 2.5, 'o': 2.4,
                          'b': 1.9, 'w': 1.9, 'f': 1.6, 'k': 1.6, 'z': 1.1,
                          'p': 0.7, 'v': 0.7, 'j': 0.3, 'y': 0.1, 'x': 0.1, 'q': 0.0}

    total_frequency = sum(german_frequencies.values())

    result = []
    for key in range(26):
        decrypted_text = decrypt(plaintext, key)

        decrypted_frequencies = {char: decrypted_text.count(char) / len(decrypted_text) * 100 for char in
                                 german_frequencies}

        similarity = sum(abs(german_frequencies[char] - decrypted_frequencies[char]) for char in
                         german_frequencies) / total_frequency

        result.append((key, decrypted_text, similarity))

    result.sort(key=lambda x: x[2])

    return [item[1] for item in result[:elements]]


print(encrypt("hallo", 1))
print(decrypt("ibmmp", 1))
print(crack("ibmmp", elements=6))
