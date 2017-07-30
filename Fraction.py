class Fraction:
    def __init__(self, numerator, denominator = 1):
        self.numerator = numerator
        self.denominator = denominator
    def __str__(self):
        return "%d/%d" %(self.numerator, self.denominator)
    def __mul__(self, other):
        return (str(self.numerator * other.numerator)+ '/' + str(self.denominator * other.denominator))

print Fraction(3) * Fraction(2,6)