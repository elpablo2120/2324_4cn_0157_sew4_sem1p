"""
__author__ = "Paul Waldecker"
__email__ = "0157@htl.rennweg.at"
__version__ = "2.0"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Finished"
"""

from collections import Counter
from Caesar import Caesar


class Vigenere:

    def __init__(self, key: str = 'a'):
        """
        Konstruktor

        :param key: Schlüssel
        """
        self.__key = key

    @property
    def get_key(self) -> str:
        """
        Diese Methode gibt den Schlüssel zurück.

        :return: Schlüssel
        """
        return self.__key

    # key: chr = property(get_key)

    def encrypt(self, plaintext: str, key: str = None) -> str:
        """
        Diese Methode verschlüsselt einen Text mit dem Vigenere-Verfahren.

        >>> en = Vigenere()
        >>> en.encrypt("Franz jagt im komplett verwahrlosten Taxi quer durch Bayern.", "StrengGeheim")
        'xkrrmpgkamuwgfgprzzzlvemzkcsfzkraefuinvvqaxgofikwke'

        :param plaintext: zu verschlüsselnder Text
        :param key: Schlüssel
        :return: Verschlüsselter Text
        """

        if key is None:
            key = self.__key

        key = Caesar().to_lowercase_letter_only(key)
        plaintext = Caesar().to_lowercase_letter_only(plaintext)

        c = Caesar()
        for i in range(len(plaintext)):
            plaintext = plaintext[:i] + c.encrypt(plaintext[i], key[i % len(key)]) + plaintext[i + 1:]

        return plaintext

    def decrypt(self, crypttext: str, key: str = None) -> str:
        """
        Diese Methode verschlüsselt einen Text mit dem Vigenere-Verfahren.

        >>> de = Vigenere()
        >>> de.decrypt("xkrrmpgkamuwgfgprzzzlvemzkcsfzkraefuinvvqaxgofikwke", "StrengGeheim")
        'franzjagtimkomplettverwahrlostentaxiquerdurchbayern'

        :param plaintext: zu verschlüsselnder Text
        :param key: Schlüssel
        :return: Verschlüsselter Text
        """

        if key is None:
            key = self.__key

        key = Caesar().to_lowercase_letter_only(key)
        crypttext = Caesar().to_lowercase_letter_only(crypttext)

        c = Caesar()
        for i in range(len(crypttext)):
            crypttext = crypttext[:i] + c.decrypt(crypttext[i], key[i % len(key)]) + crypttext[i + 1:]

        return crypttext
