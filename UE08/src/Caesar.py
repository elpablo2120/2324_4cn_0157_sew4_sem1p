"""
__author__ = "Paul Waldecker"
__email__ = "0157@htl.rennweg.at"
__version__ = "3.0"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Finished"
"""


import re
from collections import Counter

class Caesar:

    def __init__(self, key: chr = 'a'):
        """
        Konstruktor

        :param key: Schlüssel
        """
        self.__key = key

    def get_key(self) -> chr:
        """
        Diese Methode gibt den Schlüssel zurück.

        :return: Schlüssel
        """
        return self.__key

    key: chr = property(get_key)

    def to_lowercase_letter_only(self, plaintext: str) -> str:
        """Wandelt den plaintext in Kleinbuchstaben um und entfernt alle Zeichen, die keine
        Kleinbuchstaben aus dem Bereich [a..z] sind.
        >>> caesar = Caesar()
        >>> caesar.to_lowercase_letter_only("Wandelt den plaintext in Kleinbuchstaben um und entfernt alle Zeichen, die keine Kleinbuchstaben aus dem Bereich [a..z] sind.")
        'wandeltdenplaintextinkleinbuchstabenumundentferntallezeichendiekeinekleinbuchstabenausdembereichazsind'
        """
        return ''.join([c.lower() for c in plaintext if re.compile('[a-zA-Z]').match(c)])

    def encrypt(self, plaintext: str, key: str = None) -> str:
        """key ist ein Buchstabe, der definiert, um wieviele Zeichen verschoben wird.
        Falls kein key übergeben wird, nimmt übernimmt encrypt den Wert vom Property.
        >>> caesar=Caesar("b")
        >>> caesar.key
        'b'
        >>> caesar.encrypt("hallo")
        'ibmmp'
        >>> caesar.decrypt("ibmmp")
        'hallo'
        >>> caesar.encrypt("hallo", "c")
        'jcnnq'
        >>> caesar.encrypt("xyz", "c")
        'zab'
        """
        if key is None:
            key = self.__key

        key = key.lower()
        plaintext = self.to_lowercase_letter_only(plaintext)

        for i in range(len(plaintext)):
            if plaintext[i].isalpha():
                plaintext = plaintext[:i] + chr((ord(plaintext[i]) + (ord(key) - 97) - 97) % 26 + 97) + plaintext[
                                                                                                        i + 1:]

        return plaintext

    def decrypt(self, crypttext: str, key=None) -> str:
        """
        Diese Methode entschlüsselt einen Text mit dem Caesar-Verfahren.

        >>> c = Caesar("b")
        >>> c.decrypt("cde")
        'bcd'

        >>> c.decrypt("EFG", "E")
        'abc'

        :param plaintext: zu entschlüsselnder Text
        :param key: Schlüssel
        :return: Entschlüsselter Text
        """
        if key is None:
            key = self.__key

        key = key.lower()
        crypttext = self.to_lowercase_letter_only(crypttext)

        return self.encrypt(crypttext, chr((ord('a') - ord(key)) % 26 + ord('a')))



    def crack(self, crypttext: str, elements: int = 1) -> list[str]:
        """
        >>> str = 'Vor einem großen Walde wohnte ein armer Holzhacker mit seiner Frau und seinen zwei Kindern; das Bübchen hieß Hänsel und das Mädchen Gretel. Er hatte wenig zu beißen und zu brechen, und einmal, als große Teuerung ins Land kam, konnte er das tägliche Brot nicht mehr schaffen. Wie er sich nun abends im Bette Gedanken machte und sich vor Sorgen herumwälzte, seufzte er und sprach zu seiner Frau: "Was soll aus uns werden? Wie können wir unsere armen Kinder ernähren da wir für uns selbst nichts mehr haben?"'
        >>> caesar = Caesar()
        >>> caesar.crack(str)
        ['a']
        >>> caesar.crack(str, 100) # mehr als 26 können es nicht sein.
        ['a', 'j', 'n', 'o', 'e', 'w', 'd', 'q', 'z', 'p', 'i', 'h', 'y', 's', 'k', 'x', 'c', 'v', 'g', 'b', 'r', 'l']
        >>> crypted = caesar.encrypt(str, "y")
        >>> caesar.crack(crypted, 3)
        ['y', 'h', 'l']
        """
        if not isinstance(elements, int):
            raise ValueError("elements must be an integer.")
        elif elements < 1:
            raise ValueError("elements must be greater than 0")
        elif elements > 26:
            elements = 26

        return [self.decrypt(key, 'e') for key, _ in
                Counter(self.to_lowercase_letter_only(crypttext)).most_common(elements)]
