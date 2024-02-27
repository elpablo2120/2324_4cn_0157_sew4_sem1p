"""
__author__ = "Paul Waldecker"
__email__ = "0157@htl.rennweg.at"
__version__ = "1.0.0"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Development"
"""
import re


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
            ciphertext += chr((ord(c) - ord('a') + key) % 26  + ord('a'))
        return ciphertext

    def decrypt(self, ciphertext: str, key: str = None) -> str:
        pass




# Beispielanwendungen
if __name__ == "__main__":
    import doctest

    doctest.testmod()
    ceasar = Caesar()
    print(ceasar.encrypt("hallo"))
