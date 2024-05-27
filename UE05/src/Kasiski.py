"""
__author__ = "Paul Waldecker"
__email__ = "0157@htl.rennweg.at"
__version__ = "4.5"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Finished"
"""
from builtins import str
from collections import Counter
from Caesar import Caesar
from Vigenere import Vigenere


class Kasiski:

    def __init__(self, crypttext: str = ""):
        """
        Konstruktor

        :param crypttext: Geheimtext
        """
        self.__crypttext = crypttext

    @property
    def get_crypttext(self) -> str:
        """
        Diese Methode gibt den Crypttext zurück.

        :return: Crypttext
        """
        return self.__crypttext

    #crypttext: str = property(get_crypttext)

    def allpos(self, text: str, teilstring: str) -> list[int]:
        """
        Berechnet die Positionen von teilstring in text.
        Usage examples:
        >>> k = Kasiski()
        >>> k.allpos("heissajuchei, ein ei", "ei")
        [1, 10, 14, 18]
        >>> k.allpos("heissajuchei, ein ei", "hai")
        []
        """
        return [i for i in range(len(text)) if text[i:i + len(teilstring)] == teilstring]

    def alldist(self, text: str, teilstring: str) -> set[int]:
        """
        Berechnet die Abstände zwischen den Wiederholungen des Teilstrings im verschlüsselten Text.
        Usage examples:
        >>> k = Kasiski()
        >>> k.alldist("heissajuchei, ein ei", "ei")
        {4, 8, 9, 13, 17}
        >>> k.alldist("heissajuchei, ein ei", "hai")
        {}
        """
        dist = {j - i for i in self.allpos(text, teilstring) for j in self.allpos(text, teilstring) if i < j}
        if dist == set():
            return {}

        return dist

    def dist_n_tuple(self, text: str, laenge: int) -> set[tuple[str, int]]:
        """
        Überprüft alle Teilstrings aus text mit der gegebenen laenge und liefert ein Set
        mit den Abständen aller Wiederholungen der Teilstrings in text.
        Usage examples:
        >>> k = Kasiski()
        >>> k.dist_n_tuple("heissajuchei", 2) == {('ei', 9), ('he', 9)}
        True
        >>> k.dist_n_tuple("heissajuchei", 3) == {('hei', 9)}
        True
        >>> k.dist_n_tuple("heissajuchei", 4) == set()
        True
        >>> k.dist_n_tuple("heissajucheieinei", 2) == \
        {('ei', 5), ('ei', 14), ('ei', 3), ('ei', 9), ('ei', 11), ('he', 9), ('ei', 2)}
        True
        """
        return {(text[i:i + laenge], j - i) for i in range(len(text) - laenge + 1) for j in range(i + laenge, len(text))
                if text[i:i + laenge] == text[j:j + laenge]}

    # for i in range(len(text) - laenge + 1)
    #   for j in range(i + laenge, len(text))
    #       if text[i:i + laenge] == text[j:j + laenge]
    #           (text[i:i + laenge], j - i)


    def dist_n_list(self, text: str, laenge: int) -> list[int]:
        """
        Wie dist_tuple, liefert aber nur eine aufsteigend sortierte Liste der
        Abstände ohne den Text zurück. In der Liste soll kein Element mehrfach vorkommen.
        Usage examples:
        >>> k = Kasiski()
        >>> k.dist_n_list("heissajucheieinei", 2) == [2, 3, 5, 9, 11, 14]
        True
        >>> k.dist_n_list("heissajucheieinei", 3) == [9]
        True
        >>> k.dist_n_list("heissajucheieinei", 4) == []
        True
        """
        return sorted(set([j - i for i in range(len(text) - laenge + 1) for j in range(i + laenge, len(text)) if
                           text[i:i + laenge] == text[j:j + laenge]]))

    def ggt(self, x: int, y: int) -> int:
        """
        Ermittelt den größten gemeinsamen Teiler von x und y.
        Usage examples:
        >>> k = Kasiski()
        >>> k.ggt(10, 25)
        5
        >>> k.ggt(12, 14)
        2
        """
        while y != 0:
            x, y = y, x % y
        return x

    def ggt_count(self, zahlen: list[int]) -> Counter:
        """
        Bestimmt die Häufigkeit der paarweisen ggt aller Zahlen aus list.
        Usage examples:
        >>> k = Kasiski()
        >>> k.ggt_count([12, 14, 16])
        Counter({2: 2, 12: 1, 4: 1, 14: 1, 16: 1})
        >>> k.ggt_count([10, 25, 50, 100])
        Counter({10: 3, 25: 3, 50: 2, 5: 1, 100: 1})
        """
        c = Counter()
        for i in range(len(zahlen)):
            for j in range(i, len(zahlen)):
                c[self.ggt(zahlen[i], zahlen[j])] += 1
        return c

    def get_nth_letter(self, s: str, start: int, n: int) -> str:
        """
        Extrahiert aus s jeden n. Buchstaben beginnend mit index start.
        Usage examples:
        >>> k = Kasiski()
        >>> k.get_nth_letter("Das ist kein kreativer Text.", 1, 4)
        'asektrx'
        """
        return s[start::n]

    def crack_key(self, len: int):
        """
        Diese Methode liefert den Wahrscheinlichsten schlüssel zurück.
        Usage examples:
        >>> k = Kasiski("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
        >>> k.crack_key(5)
        'aaaaa'
        """
        c = Caesar()
        crypttxt = c.to_lowercase_letter_only(self.__crypttext)

        partstr = [self.get_nth_letter(crypttxt, i, len) for i in range(len)]

        return ''.join([c.crack(partstr[i], 1)[0] for i in range(len)])


if __name__ == "__main__":
    # Attacke auf Vigenere
    v = Vigenere()
    str = "Die geheime Botschaft, die ich Ihnen übermitteln muss, ist von äußerster Wichtigkeit und erfordert höchste Diskretion. Bitte nehmen Sie sich einen Moment Zeit, um diese Nachricht sorgfältig zu lesen und die Anweisungen genau zu befolgen. Unsere Zusammenarbeit und der Erfolg unserer Mission hängen davon ab. Zuerst möchte ich Sie darüber informieren, dass wir dringend ein Treffen benötigen. Dieses Treffen soll um Mitternacht stattfinden, an einem Ort, den wir im Voraus festgelegt haben. Die genauen Koordinaten werden Ihnen zu gegebener Zeit mitgeteilt. Es ist von größter Bedeutung, dass Sie pünktlich und unerkannt erscheinen.Zudem ist es unerlässlich, dass Sie den Schlüssel mitbringen. Dieser Schlüssel ist nicht nur physischer Natur, sondern symbolisiert auch die Verbindung zwischen unseren Bemühungen und dem Erfolg unserer Operation. Bewahren Sie ihn sicher auf und teilen Sie ihn mit niemandem. Bitte seien Sie äußerst wachsam und achten Sie auf verdächtige Aktivitäten. Unsere Feinde sind überall und wir müssen sicherstellen, dass wir nicht von ihnen belauscht oder entdeckt werden. Jegliche Unregelmäßigkeiten müssen sofort gemeldet werden.Das vereinbarte Zeichen wird Ihnen helfen, uns zu identifizieren. Bitte beachten Sie es sorgfältig und verwenden Sie es, um sich zu vergewissern, dass Sie mit der richtigen Person sprechen.Ich vertraue darauf, dass Sie diese Anweisungen verstehen und umsetzen können. Unsere gemeinsamen Ziele erfordern Zusammenarbeit und Engagement. Möge der Erfolg auf unserer Seite sein. Bis bald, und bleiben Sie wachsam."
    x = v.encrypt(str, "gustavo")
    k = Kasiski(x)
    len = k.ggt_count([k.dist_n_list(x, i) for i in range(3, 10)][0]).most_common(1)[0][0]
    key = k.crack_key(len)
    print(x)

    print(key)

    print(v.decrypt(x, key))
