"""
__author__ = "Paul Waldecker"
__email__ = "0157@htl.rennweg.at"
__version__ = "1.3"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Development"
"""


class Fraction:
    """
    Eine Klasse, die Brüche repräsentiert.
    :meth:`__init__` Initialisiert ein Fraction-Objekt.
    :meth:`__str__` Gibt den Bruch als Zeichenkette zurück.
    :meth:`__repr__` Gibt eine Repräsentation des Bruchs zurück.
    :meth:`__add__` Addiert zwei Brüche.
    :meth:`__radd__` Verweist auf Addition. Wird genutzt um Bruch mit int zu addieren.
    :meth:`__sub__` Subtrahiert zwei Brüche.
    :meth:`__mul__` Multipliziert zwei Brüche.
    :meth:`__truediv__` Dividiert zwei Brüche.
    :meth:`__float__` Gibt den Bruch als Gleitkommazahl zurück.
    :meth:`_simplify` Vereinfacht den Bruch.
    :meth:`_gcd` Berechnet den größten gemeinsamen Teiler von a und b.
    :meth:`numerator` Getter für den Zähler des Bruchs.
    :meth:`denominator` Getter für den Nenner des Bruchs.
    :meth:`numerator` Setter für den Zähler des Bruchs.
    :meth:`denominator` Setter für den Nenner des Bruchs.
    """

    def __init__(self, numerator=0, denominator=1):
        """
        Initialisiert ein Fraction-Objekt.
        :param self: Fraction-Objekt.
        :param numerator: Zähler des Bruchs (Standardwert ist 0).
        :param denominator: Nenner des Bruchs (Standardwert ist 1).
        :raises ArithmeticError: Falls der Nenner 0 ist.
        :return: None
        >>> f = Fraction(1)
        >>> f.numerator
        1
        >>> f.denominator
        1
        >>> f = Fraction()
        >>> f.numerator
        0
        >>> f.denominator
        1
        >>> f = Fraction(1, 0)
        Traceback (most recent call last):
        ...
        ArithmeticError: Denominator cannot be zero.
        """
        if denominator == 0:
            raise ArithmeticError("Denominator cannot be zero.")
        self._numerator = numerator
        self._denominator = denominator
        self._simplify()

    @property
    def numerator(self):
        """
        Getter für den Zähler des Bruchs.
        """
        return self._numerator

    @property
    def denominator(self):
        """
        Getter für den Nenner des Bruchs.
        """
        return self._denominator

    @numerator.setter
    def numerator(self, value):
        """
        Setzt den Zähler des Bruchs auf den angegebenen Wert und vereinfacht den Bruch.
        :param value: Der Wert, auf den der Zähler gesetzt werden soll.
        """
        self._numerator = value
        self._simplify()

    @denominator.setter
    def denominator(self, value):
        """
        Setzt den Nenner des Bruchs auf den angegebenen Wert und vereinfacht den Bruch.
        :param value: Der Wert, auf den der Nenner gesetzt werden soll.
        """
        self._denominator = value
        self._simplify()

    def _simplify(self):
        """
        Vereinfacht den Bruch.
        :return: Gekürzer Bruch.
        >>> f = Fraction(6, 9)
        >>> print(f)
        2/3
        """
        gcd = self._gcd(self._numerator, self._denominator)
        self._numerator //= gcd
        self._denominator //= gcd

    def _gcd(self, a, b):
        """
        Berechnet den größten gemeinsamen Teiler von a und b.
        :param a: Numerator
        :param b: Denominator
        :return: Größter gemeinsamer Teiler von a und b.
        >>> f = Fraction()
        >>> f._gcd(6, 9)
        3
        >>> f = Fraction()
        >>> f._gcd(-6, 9)
        3
        """
        while b != 0:
            a, b = b, a % b
        return a

    def __str__(self):
        """
        Gibt den Bruch als Zeichenkette zurück.
        :param self: Fraction-Objekt.
        :return: Bruch als Zeichenkette.
        >>> f = Fraction(1, 2)
        >>> print(f)
        1/2
        >>> f = Fraction(2, 2)
        >>> print(f)
        1
        >>> f = Fraction(3, 2)
        >>> print(f)
        1 1/2
        >>> f = Fraction(0, 2)
        >>> print(f)
        0
        >>> f = Fraction(10, 1)
        >>> print(f)
        10
        """
        if self._numerator == 0:
            return '0'
        elif self._denominator == 1:
            return str(self._numerator)
        elif abs(self._numerator) < abs(self._denominator):
            return f"{self._numerator}/{self._denominator}"
        elif self._numerator < 0 and self._denominator > 0:
                whole_part = abs(self._numerator) // abs(self._denominator)
                remainder = abs(self._numerator) % abs(self._denominator)
                whole_part *= -1
                if remainder == 0:
                    return str(whole_part)
                else:
                    return f"{whole_part} {remainder}/{self._denominator}"
        elif self._numerator > 0 and self._denominator < 0:
                whole_part = abs(self._numerator) // abs(self._denominator)
                remainder = abs(self._numerator) % abs(self._denominator)
                whole_part *= -1
                if remainder == 0:
                    return str(whole_part)
                else:
                    return f"{whole_part} {remainder}/{self._denominator}"
        else:
            whole_part = self._numerator // self._denominator
            remainder = self._numerator % self._denominator
            if remainder == 0:
                return str(whole_part)
            else:
                return f"{whole_part} {remainder}/{self._denominator}"

    def __repr__(self):
        """
        Gibt eine Repräsentation des Bruchs zurück.
        >>> f = Fraction(1, 2)
        >>> print(repr(f))
        Fraction(1, 2)
        """
        return f"Fraction({self._numerator}, {self._denominator})"

    def __add__(self, other):
        """
        Addiert zwei Brüche.
        :param other: Der Bruch, der addiert werden soll.
        :return: addierter Bruch.
        >>> f1 = Fraction(1, 2)
        >>> f2 = Fraction(1, 3)
        >>> f3 = Fraction(-1, 6)
        >>> f4 = f1 + f2
        >>> print(f4)
        5/6
        >>> f5 = f1 + f3
        >>> print(f5)
        1/3
        >>> f6 = f1 + f1
        >>> print(f6)
        1
        >>> f7 = f1 + 1
        >>> print(f7)
        1 1/2
        >>> f8 = -1 + f1
        >>> print(f8)
        -1/2
        """

        if isinstance(other, int):
            other = Fraction(other, 1)

        if isinstance(other, Fraction):
            new_numerator = self._numerator * other._denominator + other._numerator * self._denominator
            new_denominator = self._denominator * other._denominator
            return Fraction(new_numerator, new_denominator)
        else:
            raise NotImplementedError

    def __radd__(self, other):
        """
        Verweist auf Addition. Wird genutzt um Bruch mit int zu addieren.
        :param other: Bruch oder int.
        :return: addierter Bruch.
        """
        return self.__add__(other)

    def __sub__(self, other_fraction):
        """
        Subtrahiert zwei Brüche.
        :param other_fraction: Der Bruch, der subtrahiert werden soll.
        :return: subtrahierter Bruch.
        >>> f1 = Fraction(1, 2)
        >>> f2 = Fraction(1, 3)
        >>> f3 = Fraction(-1, 2)
        >>> f4 = Fraction(-1, -3)
        >>> f5 = f1 - f2
        >>> print(f5)
        1/6
        >>> f6 = f1 - f3
        >>> print(f6)
        1
        >>> f7 = f3 - f4
        >>> print(f7)
        -5/6
        >>> f8 = f3 - f3
        >>> print(f8)
        0
        """
        new_denominator = self._denominator * other_fraction._denominator
        new_numerator = self._numerator * other_fraction._denominator - other_fraction._numerator * self._denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other_fraction):
        """
        Multipliziert zwei Brüche.
        :param other_fraction: Der Bruch, der multipliziert werden soll.
        :return: multiplizierter Bruch.
        >>> f1 = Fraction(1, 2)
        >>> f2 = Fraction(1, 3)
        >>> f3 = Fraction(-1, 2)
        >>> f4 = Fraction(-1, -3)
        >>> f5 = f1 * f2
        >>> print(f5)
        1/6
        >>> f6 = f1 * f3
        >>> print(f6)
        -1/4
        >>> f7 = f3 * f4
        >>> print(f7)
        -1/6
        >>> f8 = f3 * f3
        >>> print(f8)
        1/4
        """
        new_numerator = self._numerator * other_fraction._numerator
        new_denominator = self._denominator * other_fraction._denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other_fraction):
        """
        Dividiert zwei Brüche.
        :param other_fraction: Der Bruch, der dividiert werden soll.
        :return: dividierter Bruch.
        >>> f1 = Fraction(1, 2)
        >>> f2 = Fraction(1, 3)
        >>> f3 = Fraction(-1, 2)
        >>> f4 = Fraction(-1, -3)
        >>> f5 = f1 / f2
        >>> print(f5)
        1 1/2
        >>> f6 = f1 / f3
        >>> print(f6)
        -1
        >>> f7 = f3 / f4
        >>> print(f4)
        1/3
        >>> print(f7)
        -1 1/2
        >>> f8 = f3 / f3
        >>> print(f8)
        1
        """
        new_numerator = self._numerator * other_fraction._denominator
        new_denominator = self._denominator * other_fraction._numerator
        return Fraction(new_numerator, new_denominator)

    def __float__(self):
        """
        Gibt den Bruch als Gleitkommazahl zurück.
        :return: Bruch als Gleitkommazahl.
        >>> f = Fraction(11, 12)
        >>> float(f)
        0.9166666666666666
        """
        return self._numerator / self._denominator


if __name__ == '__main__':
    f1 = Fraction(-1, 2)
    f2 = Fraction(-1, -3)
    print(f1/f2)
    import doctest

    doctest.testmod()

