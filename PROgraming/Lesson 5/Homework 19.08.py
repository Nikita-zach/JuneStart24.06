class ProperFraction:
    def __init__(self, num: int, den: int):
        if den == 0:
            raise ValueError("Denominator cannot be zero.")
        self.num = num
        self.den = den

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __eq__(self, other):
        return self.num * other.den == other.num * self.den

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.num * other.den < other.num * self.den

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return self.num * other.den > other.num * self.den

    def __ge__(self, other):
        return self > other or self == other

    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return ProperFraction(new_num, new_den)

    def __sub__(self, other):
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return ProperFraction(new_num, new_den)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return ProperFraction(new_num, new_den)


frac1 = ProperFraction(1, 2)
frac2 = ProperFraction(1, 3)

print(f"Sum: {frac1 + frac2}")
print(f"Difference: {frac1 - frac2}")
print(f"Multiply: {frac1 * frac2}")

print(f"Is fraction 1 equal to fraction 2? {frac1 == frac2}")
print(f"Is fraction 1 not equal to fraction 2? {frac1 != frac2}")
print(f"Is fraction 1 less than to fraction 2? {frac1 < frac2}")
print(f"Is fraction 1 greater than to fraction 2? {frac1 > frac2}")
print(f"Is fraction 1 less than or equal to fraction 2? {frac1 <= frac2}")
print(f"Is fraction 1 greater than or equal to fraction 2? {frac1 >= frac2}")
