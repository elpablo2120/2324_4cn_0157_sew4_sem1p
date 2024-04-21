class Fraction:
    '''
    Class to represent fractions.
    '''
    def __init__(self, numerator=0, denominator=1):
        """
        Class to represent fractions.
        :param numerator: The numerator of the fraction (optional, default is 0).
        :param denominator: The denominator of the fraction (optional, default is 1).
        :raise ArithmeticError: If the denominator is 0.
        :return: A simplified Fraction object.
        >>> f1 = Fraction(3, -6); str(f1)
        '-1/2'
        >>> f2 = Fraction(7); str(f2)
        '7'
        >>> f3 = Fraction(6,3); str(f3)
        '2'
        """
        if denominator == 0:
            raise ArithmeticError("Denominator cannot be zero.")
        self._numerator = numerator
        self._denominator = denominator
        self._simplify()

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    @numerator.setter
    def numerator(self, value):
        self._numerator = value
        self._simplify()

    @denominator.setter
    def denominator(self, value):
        self._denominator = value
        self._simplify()

    def _simplify(self):
        gcd = self._gcd(self._numerator, self._denominator)
        self._numerator //= gcd
        self._denominator //= gcd

    def _gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def __str__(self):
        if self._numerator == 0:
            return '0'
        elif self._denominator == 1:
            return str(self._numerator)
        elif abs(self._numerator) < abs(self._denominator):
            return f"{self._numerator}/{self._denominator}"
        else:
            whole_part = self._numerator // self._denominator
            remainder = abs(self._numerator) % abs(self._denominator)
            return f"{whole_part} {remainder}/{self._denominator}"

    def __repr__(self):
        return f"Fraction({self._numerator}, {self._denominator})"

    def __add__(self, other_fraction):
        new_denominator = self._denominator * other_fraction._denominator
        new_numerator = self._numerator * other_fraction._denominator + other_fraction._numerator * self._denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other_fraction):
        new_denominator = self._denominator * other_fraction._denominator
        new_numerator = self._numerator * other_fraction._denominator - other_fraction._numerator * self._denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other_fraction):
        new_numerator = self._numerator * other_fraction._numerator
        new_denominator = self._denominator * other_fraction._denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other_fraction):
        new_numerator = self._numerator * other_fraction._denominator
        new_denominator = self._denominator * other_fraction._numerator
        return Fraction(new_numerator, new_denominator)


# Example usage
print('Usage:')
f1 = Fraction(-31, 62)
f2 = Fraction(-1, )
print(f1 + f2)  # Output: 5/6
print(f1 - f2)  # Output: 1/6
print(f1 * f2)  # Output: 1/6
print(f1 / f2)  # Output: 1 1/2

print(f1.numerator)
print(f1.denominator)