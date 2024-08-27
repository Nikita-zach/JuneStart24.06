import math


class ProperFraction:
    def __init__(self, numerator: int, denominator: int):
        if not isinstance(numerator, int):
            raise ValueError("Numerator must be integer")
        if not isinstance(denominator, int):
            raise ValueError("Denominator must be integer")

        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")

        # Adjust the sign of the denominator
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        # Reduce the fraction
        gcd = math.gcd(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    def __str__(self):
        if self.denominator == 1:
            return f"{self.numerator}"
        return f"{self.numerator}/{self.denominator}"

    def __eq__(self, other):
        if not isinstance(other, ProperFraction):
            return NotImplemented
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, ProperFraction):
            return NotImplemented
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        if not isinstance(other, ProperFraction):
            return NotImplemented
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other):
        return self > other or self == other

    def __add__(self, other):
        if not isinstance(other, ProperFraction):
            return NotImplemented
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return ProperFraction(new_numerator, new_denominator)

    def __sub__(self, other):
        if not isinstance(other, ProperFraction):
            return NotImplemented
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return ProperFraction(new_numerator, new_denominator)

    def __mul__(self, other):
        if not isinstance(other, ProperFraction):
            return NotImplemented
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return ProperFraction(new_numerator, new_denominator)


frac1 = ProperFraction(1, 2)
frac2 = ProperFraction(1, 3)

print(f"Sum: {frac1 + frac2}")
print(f"Difference: {frac1 - frac2}")
print(f"Multiply: {frac1 * frac2}")

print(f"Is fraction 1 equal to fraction 2? {frac1 == frac2}")
print(f"Is fraction 1 not equal to fraction 2? {frac1 != frac2}")
print(f"Is fraction 1 less than fraction 2? {frac1 < frac2}")
print(f"Is fraction 1 greater than fraction 2? {frac1 > frac2}")
print(f"Is fraction 1 less than or equal to fraction 2? {frac1 <= frac2}")
print(f"Is fraction 1 greater than or equal to fraction 2? {frac1 >= frac2}")
