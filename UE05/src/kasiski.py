"""
__author__ = "Paul Waldecker"
__email__ = "0157@htl.rennweg.at"
__version__ = "1.0.0"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Development"
"""
import re
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
        >>> caesar=Caesar("a")
        >>> caesar.key
        'a'
        >>> caesar.encrypt("hallo")
        'ibmmp'
        >>> caesar.encrypt("hallo", "c")
        'kdoor'
        >>> caesar.encrypt("xyz", "c")
        'abc'
        """
        if key is None:
            key = self.key
        if isinstance(key, str) and len(key) == 1 and key.islower():
            key = ord(key) - ord('a') + 1
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
        >>> caesar=Caesar("a")
        >>> caesar.key
        'a'
        >>> caesar.decrypt("ibmmp")
        'hallo'
        >>> caesar.decrypt("kdoor", "c")
        'hallo'
        >>> caesar.decrypt("abc", "c")
        'xyz'
        """
        if key is None:
            key = self.key
        if isinstance(key, str) and len(key) == 1 and key.islower():
            key = ord(key) - ord('a') + 1
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
        crypttext = self.to_lowercase_letter_only(crypttext)
        possible_keys = []
        frequencies = {}
        for char in crypttext:
            frequencies[char] = frequencies.get(char, 0) + 1
        sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
        most_common_char_crypt = sorted_frequencies[0][0]
        for most_common_char in "etaoinshrdlcumwfgypbvkjxqz":
            key = (ord(most_common_char_crypt) - ord(most_common_char)) % 26
            decrypted_text = self.decrypt(crypttext, key)
            possible_keys.append(decrypted_text)

        return possible_keys[:elements]


# Beispielanwendungen
if __name__ == "__main__":
    import doctest

    doctest.testmod()
    ceasar = Caesar()
    print(ceasar.encrypt("hallo"))
    print(ceasar.decrypt("ibmmp"))
    print(ceasar.crack("ibmmp"))
