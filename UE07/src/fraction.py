class Bruch:
    '''
    Klasse zur Repräsentation von Brüchen.
    '''
    def __init__(self, zaehler=0, nenner=1):
        """
        Klasse zur Repräsentation von Brüchen.
        :param zaehler: Der Zähler des Bruchs (optional, Standardwert ist 0).
        :param nenner: Der Nenner des Bruchs (optional, Standardwert ist 1).
        :raise ArithmeticError: Wenn der Nenner 0 ist.
        :return: Ein gekürztes Bruch-Objekt.
        >>> b1 = Bruch(3, -6); str(b1)
        '-1/2'
        >>> b2 = Bruch(7); str(b2)
        '7'
        >>> b3 = Bruch(6,3); str(b3)
        '2'
        """
        if nenner == 0:
            raise ArithmeticError("Nenner darf nicht null sein.")
        self._zaehler = zaehler
        self._nenner = nenner
        self._kuerzen()

    def _kuerzen(self):
        ggT = self._ggT(self._zaehler, self._nenner)
        self._zaehler //= ggT
        self._nenner //= ggT

    def _ggT(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def __str__(self):
        if self._zaehler == 0:
            return '0'
        elif self._nenner == 1:
            return str(self._zaehler)
        elif abs(self._zaehler) < abs(self._nenner):
            return f"{self._zaehler}/{self._nenner}"
        else:
            ganze_teil = self._zaehler // self._nenner
            rest = abs(self._zaehler) % abs(self._nenner)
            return f"{ganze_teil} {rest}/{self._nenner}"

    def __repr__(self):
        return f"Bruch({self._zaehler}, {self._nenner})"

# Beispielverwendung
print('Anwendung:')
b1 = Bruch(3, 6)
print(b1)  # Ausgabe: 1/2
b2 = Bruch(7)
print(b2)  # Ausgabe: 7
