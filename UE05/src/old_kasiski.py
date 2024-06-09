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
    """
    Caesar cipher class.
    """

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
        :param plaintext: Der zu bereinigende Klartext als Zeichenkette.
        :return: Der bereinigte Klartext als Zeichenkette.
        >>> caesar = Caesar()
        >>> caesar.to_lowercase_letter_only("Wandelt den plaintext in Kleinbuchstaben um und entfernt alle Zeichen, die keine Kleinbuchstaben aus dem Bereich [a..z] sind.")
        'wandeltdenplaintextinkleinbuchstabenumundentferntallezeichendiekeinekleinbuchstabenausdembereichazsind'
        """
        return re.sub('[^a-z]', "", plaintext.lower())

    def encrypt(self, plaintext: str, key: str = None) -> str:
        """
        key ist ein Buchstabe, der definiert, um wieviele Zeichen verschoben wird.
        Falls kein key übergeben wird, nimmt übernimmt encrypt den Wert vom Property.
        :param plaintext: Der zu verschlüsselnde Klartext als Zeichenkette.
        :param key: Der Verschlüsselungsschlüssel (optional, Standardwert ist None).
        :return: Der Geheimtext als Zeichenkette.
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
        :param ciphertext: Der zu entschlüsselnde Geheimtext als Zeichenkette.
        :param key: Der Verschlüsselungsschlüssel (optional, Standardwert ist None).
        :return: Der Klartext als Zeichenkette.
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


class Vigenere:
    """
    Vigenere cipher class.
    """

    def __init__(self, key: str = "a"):
        """
        Konstruktor der Klasse Vigenere.
        :param key: Schlüssel für die Verschlüsselung (optional, Standardwert ist "a").
        """
        self.key = key

    def encrypt(self, plaintext: str, key: str = None) -> str:
        """
        Verschlüsselt den gegebenen Klartext mit Vigenere und dem gegebenen Schlüssel.
        :param plaintext: Der zu verschlüsselnde Klartext als Zeichenkette.
        :param key: Der Verschlüsselungsschlüssel (optional, Standardwert ist None).
        :return: Der Geheimtext als Zeichenkette.
        >>> vigenere = Vigenere("b"); vigenere.key
        'b'
        >>> vigenere2 = Vigenere("hugo");vigenere2.encrypt("Hallo, wie geht es dir?")
        'ourzvqosnynhlmjwy'
        >>> vigenere2 = Vigenere("SPAM");vigenere2.encrypt("HalloWELT")
        'zplxglexl'
        """

        if key is None:
            key = self.key

        key = key.lower()
        caesar = Caesar()
        plaintext = caesar.to_lowercase_letter_only(plaintext)
        return ''.join([caesar.encrypt(plaintext[i], key[i % len(key)]) for i in range(len(plaintext))])

    def decrypt(self, crypttext: str, key: str = None) -> str:
        """
        Decrypts the given crypttext with Vigenere and the given key.
        :param crypttext: Der zu entschlüsselnde Geheimtext als Zeichenkette.
        :param key: Der Verschlüsselungsschlüssel (optional, Standardwert ist None).
        :return: Der Klartext als Zeichenkette.
        >>> vigenere = Vigenere("b"); vigenere.key
        'b'
        >>> vigenere2 = Vigenere("hugo");vigenere2.decrypt("ourzvqosnynhlmjwy")
        'hallowiegehtesdir'
        """

        if key is None:
            key = self.key

        key = key.lower()
        caesar = Caesar()
        return ''.join([caesar.decrypt(crypttext[i], key[i % len(key)]) for i in range(len(crypttext))])


# Beispielanwendungen
if __name__ == "__main__":
    import doctest

    doctest.testmod()
    ceasar = Caesar()
    print(ceasar.encrypt("hallo"))
    print(ceasar.decrypt("ibmmp"))
    print(ceasar.crack("ibmmp"))

    vigenere = Vigenere("hugo")
    print(vigenere.encrypt("hallo"))
    print(vigenere.decrypt("ourzv"))
