"""
__author__ = "Paul Waldecker"
__email__ = "0157@htl.rennweg.at"
__version__ = "1.0.0"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Development"
"""

def encrypt(plaintext: str, key=None) -> str:
    """
    Verschlüsselt den gegebenen Klartext mithilfe des Caesar-Verschlüsselungsverfahrens.

    :param plaintext: Der zu verschlüsselnde Klartext als Zeichenkette.
    :param key: Der Verschlüsselungsschlüssel (optional, Standardwert ist None).
    :return: Die verschlüsselte Zeichenkette.

    >>> encrypt("hallo", 1)
    'ibmmp'
    >>> encrypt("hello", 3)
    'khoor'
    """
    ciphertext = ""
    for i in plaintext:
        ciphertext += chr((ord(i) - ord('a') + key) % 26 + ord('a'))
    return ciphertext


def decrypt(plaintext: str, key=None) -> str:
    """
    Entschlüsselt den gegebenen Geheimtext mithilfe des Caesar-Verschlüsselungsverfahrens.

    :param plaintext: Der zu entschlüsselnde Geheimtext als Zeichenkette.
    :param key: Der Entschlüsselungsschlüssel (optional, Standardwert ist None).
    :return: Die entschlüsselte Zeichenkette.

    >>> decrypt("ibmmp", 1)
    'hallo'
    >>> decrypt("khoor", 3)
    'hello'
    """
    ciphertext = ""
    for i in plaintext:
        ciphertext += chr((ord(i) - ord('a') - key) % 26 + ord('a'))
    return ciphertext


def crack(plaintext: str, elements=1) -> list[str]:
    """
    Versucht, den Geheimtext mithilfe von Häufigkeitsanalysen zu entschlüsseln.

    :param plaintext: Der zu entschlüsselnde Geheimtext als Zeichenkette.
    :param elements: Die Anzahl der Top-Ergebnisse, die zurückgegeben werden sollen (optional, Standardwert ist 1).
    :return: Eine Liste von Zeichenketten, die mögliche Klartexte repräsentieren.
    """
    # Deutsch Häufigkeitsanalyse (Quelle: https://de.wikipedia.org/wiki/Buchstabenh%C3%A4ufigkeit)
    deutsche_haeufigkeiten = {'e': 17.4, 'n': 9.8, 'i': 7.6, 's': 7.3, 'r': 7.0,
                              'a': 6.2, 't': 6.1, 'd': 5.5, 'h': 5.1, 'u': 4.2,
                              'l': 3.4, 'c': 3.0, 'g': 3.0, 'm': 2.5, 'o': 2.4,
                              'b': 1.9, 'w': 1.9, 'f': 1.6, 'k': 1.6, 'z': 1.1,
                              'p': 0.7, 'v': 0.7, 'j': 0.3, 'y': 0.1, 'x': 0.1, 'q': 0.0}

    gesamt_haeufigkeit = sum(deutsche_haeufigkeiten.values())

    ergebnis = []
    for schluessel in range(26):
        entschluesselter_text = decrypt(plaintext, schluessel)

        entschluesselte_haeufigkeiten = {char: entschluesselter_text.count(char) / len(entschluesselter_text) * 100
                                          for char in deutsche_haeufigkeiten}

        aehnlichkeit = sum(abs(deutsche_haeufigkeiten[char] - entschluesselte_haeufigkeiten[char])
                           for char in deutsche_haeufigkeiten) / gesamt_haeufigkeit

        ergebnis.append((schluessel, entschluesselter_text, aehnlichkeit))

    ergebnis.sort(key=lambda x: x[2])

    return [item[1] for item in ergebnis[:elements]]


# Beispielanwendungen
if __name__ == "__main__":
    import doctest
    doctest.testmod()
