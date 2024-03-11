"""
__author__ = "Paul Waldecker"
__email__ = "0157@htl.rennweg.at"
__version__ = "1.0.0"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Development"
"""
import re
from collections import Counter
from typing import List


class Caesar:

    def __init__(self, key: int = 1):
        """
        Erzeugt eine neue Instanz der Caesar-Klasse.
        :param key: Der Verschlüsselungsschlüssel (optional, Standardwert ist None).
        """
        self.key = key

    def to_lowercase_letter_only(self, plaintext: str) -> str:
        """
        Wandelt den plaintext in Kleinbuchstaben um und entfernt alle Zeichen, die keine
        Kleinbuchstaben aus dem Bereich [a..z] sind.
        >>> caesar = Caesar()
        >>> caesar.to_lowercase_letter_only("Wandelt den plaintext in Kleinbuchstaben um und entfernt alle Zeichen, die keine Kleinbuchstaben aus dem Bereich [a..z] sind.")
        'wandeltdenplaintextinkleinbuchstabenumundentferntallezeichendiekeinekleinbuchstabenausdembereichazsind'
        """
        return re.sub('[^a-z]', "", plaintext.lower())

    def encrypt(self, plaintext: str, key: str = None) -> str:
        """
        key ist ein Buchstabe, der definiert, um wieviele Zeichen verschoben wird.
        Falls kein key übergeben wird, nimmt übernimmt encrypt den Wert vom Property.
        >>> caesar=Caesar("b")
        >>> caesar.key
        'b'
        >>> caesar.encrypt("hallo")
        'ibmmp'
        >>> caesar.encrypt("hallo", "c")
        'jcnnq'
        >>> caesar.encrypt("xyz", "c")
        'zab'
        """
        if key is None:
            key = self.key
        if isinstance(key, str) and len(key) == 1 and key.islower():
            key = ord(key) - ord('a')
        elif not isinstance(key, int):
            raise ValueError("Key must be a lowercase letter or an integer")

        plaintext = self.to_lowercase_letter_only(plaintext)
        ciphertext = ""
        for c in plaintext:
            ciphertext += chr((ord(c) - ord('a') + key) % 26 + ord('a'))
        return ciphertext

    def decrypt(self, ciphertext: str, key: str = None) -> str:
        """
        key ist ein Buchstabe, der definiert, um wieviele Zeichen verschoben wird.
        Falls kein key übergeben wird, nimmt übernimmt decrypt den Wert vom Property.
        >>> caesar=Caesar("b")
        >>> caesar.key
        'b'
        >>> caesar.decrypt("ibmmp")
        'hallo'
        >>> caesar.decrypt("jcnnq", "c")
        'hallo'
        >>> caesar.decrypt("zab", "c")
        'xyz'
        """
        if key is None:
            key = self.key
        if isinstance(key, str) and len(key) == 1 and key.islower():
            key = ord(key) - ord('a')
        elif not isinstance(key, int):
            raise ValueError("Key must be a lowercase letter or an integer")

        ciphertext = self.to_lowercase_letter_only(ciphertext)
        plaintext = ""
        for c in ciphertext:
            plaintext += chr((ord(c) - ord('a') - key) % 26 + ord('a'))
        return plaintext

    def crack(self, crypttext: str, elements: int = 1) -> List[str]:
        """
        Versucht, den Geheimtext mithilfe von Häufigkeitsanalysen zu entschlüsseln. Zr hilfe wird die häufigkeitsanalyse gezogen.

        :param crypttext: Der zu entschlüsselnde Geheimtext als Zeichenkette.
        :param elements: Die Anzahl der Top-Ergebnisse, die zurückgegeben werden sollen (optional, Standardwert ist 1).
        :return: Eine Liste von Zeichenketten, die mögliche Klartexte repräsentieren.
        >>> str='Vor einem großen Walde wohnte ein armer Holzhacker mit seiner Frau und seinen zwei Kindern; das Bübchen hieß Hänsel und das Mädchen Gretel. Er hatte wenig zu beißen und zu brechen, und einmal, als große Teuerung ins Land kam, konnte er das tägliche Brot nicht mehr schaffen. Wie er sich nun abends im Bette Gedanken machte und sich vor Sorgen herumwälzte, seufzte er und sprach zu seiner Frau: "Was soll aus uns werden? Wie können wir unsere armen Kinder ernähren da wir für uns selbst nichts mehr haben?"'
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


# Beispielanwendungen
if __name__ == "__main__":
    import doctest

    doctest.testmod()
    ceasar = Caesar()
    print(ceasar.encrypt("hallo"))
    print(ceasar.decrypt("ibmmp"))
    print(ceasar.crack("ibmmp"))
