class Bruch:
    def __init__(self, zaehler=0, nenner=1):
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
        if self._nenner == 1:
            return str(self._zaehler)
        return f"{self._zaehler}/{self._nenner}"

# Beispielverwendung
b1 = Bruch(3, 6)
print(b1)  # Ausgabe: 1/2
b2 = Bruch(7)
print(b2)  # Ausgabe: 7
