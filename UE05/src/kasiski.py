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


