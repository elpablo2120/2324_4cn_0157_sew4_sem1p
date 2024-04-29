class BritishLength:
    def __init__(self, feet=1, inches=0):
        self.total_inches = feet * 12 + inches

    @property
    def feet(self):
        if self.total_inches >= 0:
            return self.total_inches // 12
        else:
            return -(abs(self.total_inches) // 12)

    @property
    def inches(self):
        if self.total_inches >= 0:
            return self.total_inches % 12
        else:
            return -(abs(self.total_inches) % 12)

    @property
    def meters(self):
        return self.total_inches * 0.0254

    def __add__(self, other):
        total = self.total_inches + other.total_inches
        return BritishLength(0, total)

    def __sub__(self, other):
        total = self.total_inches - other.total_inches
        return BritishLength(0, total)

    def __eq__(self, other):
        if isinstance(self, BritishLength) and (other, BritishLength):
            return self.total_inches == other.total_inches
        return False

    def __str__(self):
        if self.meters == 0:
            erg_meters = int(self.meters)
        else:
            erg_meters = round(self.meters, 4)

        if self.feet == 0:
            erg_feet = ""
            unit_feet = ""
        else:
            erg_feet = self.feet
            unit_feet = " ft "

        if self.inches == 0:
            erg_inches = ""
            unit_inches = ""
        else:
            erg_inches = self.inches
            unit_inches = " in "

        if self.inches == 0 and self.feet == 0:
            erg_inches = self.inches
            unit_inches = " in "

        return f"{erg_feet}{unit_feet}{erg_inches}{unit_inches}({erg_meters}) m"


b1 = BritishLength(2, -28)
b2 = BritishLength(3, 9)

# Addition
result_addition = b1
expected_addition = BritishLength(0, -4)
print(result_addition == expected_addition)  # Sollte True sein

# Subtraktion
result_subtraction = b1 - b2
expected_subtraction = BritishLength(3, 11)
print(result_subtraction == expected_subtraction)  # Sollte True sein

