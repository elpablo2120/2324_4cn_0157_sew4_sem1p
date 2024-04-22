import re
from collections import Counter
from typing import List


class Caesar:
    """
    Caesar cipher class.
    """

    def __init__(self, key: int = 1):
        """
        Constructor.
        :param key: Key to use for encryption and decryption
        """
        self.key = key

    def to_lowercase_letter_only(self, plaintext: str) -> str:
        """
        Returns the plaintext in lowercase and without special characters.

        >>> caesar1 = Caesar(); caesar1.to_lowercase_letter_only("Hallo, wie geht es dir?")
        'hallowiegehtesdir'

        :param plaintext:
        :return:
        """

        return re.sub(r'[^a-z]', '', plaintext.lower())

    def encrypt(self, plaintext: str, key: str = None) -> str:
        """
        Encrypts the given plaintext with the given key.
        :param plaintext:
        :param key: is a letter that defines how many letters the alphabet is shifted
        if no key is given, the default key is taken by the property
        :return:

        >>> caesar = Caesar("b"); caesar.key
        'b'

        >>> caesar2 = Caesar();caesar2.encrypt("hallo")
        'ibmmp'

        >>> caesar3 = Caesar();caesar3.decrypt("ibmmp")
        'hallo'

        >>> caesar4 = Caesar();caesar4.encrypt("hallo", "c")
        'jcnnq'

        >>> caesar5 = Caesar();caesar5.encrypt("xyz", "c")
        'zab'
        """
        if key is None:
            key = self.key
        elif isinstance(key, str) and len(key) == 1 and key.islower():
            key = ord(key) - ord('a')
        elif not isinstance(key, int):
            raise ValueError("Key must be an integer or a single lowercase letter.")

        plaintext = self.to_lowercase_letter_only(plaintext)
        ciphertext = ""
        for c in plaintext:
            ciphertext += chr((ord(c) - ord('a') + key) % 26 + ord('a'))
        return ciphertext

    def decrypt(self, ciphertext: str, key: str = None) -> str:
        """
        Decrypts the given ciphertext with the given key.

        :param ciphertext:
        :param key: is a letter that defines how many letters the alphabet is shifted
        if no key is given, the default key is taken by the property
        :return:
        """
        if key is None:
            key = self.key
        elif isinstance(key, str) and len(key) == 1 and key.islower():
            key = ord(key) - ord('a')
        elif not isinstance(key, int):
            raise ValueError("Key must be an integer or a single lowercase letter.")

        ciphertext = self.to_lowercase_letter_only(ciphertext)
        plaintext = ""
        for c in ciphertext:
            plaintext += chr((ord(c) - ord('a') - key) % 26 + ord('a'))
        return plaintext

    def crack(self, crypttext: str, elements: int = 1) -> List[str]:
        """
        Calculates a List with the most likely keys for the given crypttext.

        >>> str='Vor einem großen Walde wohnte ein armer Holzhacker mit seiner Frau und seinen zwei Kindern; das Bübchen hieß Hänsel und das Mädchen Gretel. Er hatte wenig zu beißen und zu brechen, und einmal, als große Teuerung ins Land kam, konnte er das tägliche Brot nicht mehr schaffen. Wie er sich nun abends im Bette Gedanken machte und sich vor Sorgen herumwälzte, seufzte er und sprach zu seiner Frau: "Was soll aus uns werden? Wie können wir unsere armen Kinder ernähren da wir für uns selbst nichts mehr haben?"'; caeser = Caesar(); caeser.crack(str)
        ['a']

        >>> caesar = Caesar(); caesar.crack(str, 100) # mehr als 26 können es nicht sein
        ['a', 'j', 'n', 'o', 'e', 'w', 'd', 'q', 'z', 'p', 'i', 'h', 'y', 's', 'k', 'x', 'c', 'v', 'g', 'b', 'r', 'l']

        >>> crypted = caeser.encrypt(str, "y"); caesar.crack(crypted, 3)
        ['y', 'h', 'l']

        >>> caesar1 = Caesar(); caesar1.crack(caesar1.encrypt(str,'b'), 100)
        ['b']

        >>> caesar2 = Caesar(); caesar2.crack("ibmmp", 2)
        ['b', 'c']

        :param ciphertext:
        :param elements: number of elements to return
        :return:
        """

        if not isinstance(elements, int):
            raise ValueError("elements must be an integer.")
        elif elements < 1:
            raise ValueError("elements must be greater than 0")
        elif elements > 26:
            elements = 26

        return [self.decrypt(key, 'e') for key, _ in Counter(self.to_lowercase_letter_only(crypttext)).most_common(elements)]

    pass