#!/usr/local/bin/python3


class Fraction:

    def gcd (self, a, b):
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a

        return a + b

    def optimize_fraction(self,numerator, denominator):
        self.numerator = int(numerator / (self.gcd(numerator, denominator)))
        self.denominator = int(denominator / (self.gcd(numerator, denominator)))

    def __init__(self, numerator, denominator):
        self.optimize_fraction(numerator, denominator)
        self.string_fraction = str(self.numerator) + '/' + str(self.denominator)

    def __add__(self, obj):
        if self.denominator == obj.denominator:
            self.numerator = self.numerator + obj.numerator
        else:
            self.numerator = self.numerator * obj.denominator + obj.numerator * self.denominator
            self.denominator = self.denominator * obj.denominator
        self.optimize_fraction(self.numerator, self.denominator)
        self.string_fraction = str(self.numerator) + '/' + str(self.denominator)
        print(self.string_fraction)

    def __sub__(self, obj):
        if self.denominator == obj.denominator:
            self.numerator = self.numerator - obj.numerator
        else:
            self.numerator = self.numerator * obj.denominator - obj.numerator * self.denominator
            self.denominator = self.denominator * obj.denominator
        self.optimize_fraction(self.numerator, self.denominator)
        self.string_fraction = str(self.numerator) + '/' + str(self.denominator)
        print(self.string_fraction)

    def __mul__(self, obj):
        self.numerator = self.numerator * obj.numerator
        self.denominator = self.denominator * obj.denominator
        self.optimize_fraction(self.numerator, self.denominator)
        self.string_fraction = str(self.numerator) + '/' + str(self.denominator)
        print(self.string_fraction)

    def __truediv__(self, obj):
        self.numerator = self.numerator * obj.denominator
        self.denominator = self.denominator * obj.numerator
        self.optimize_fraction(self.numerator, self.denominator)
        self.string_fraction = str(self.numerator) + '/' + str(self.denominator)
        print(self.string_fraction)


if __name__ == '__main__':

    fraction1 = Fraction(1, 2)
    fraction1 + Fraction(5, 8)
    fraction1 * Fraction(1, 2)
    fraction1 / Fraction(7, 8)

