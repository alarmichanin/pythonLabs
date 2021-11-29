from math import gcd


class Rational:
    """
        Class consists of two part of fraction (numerator and denominator)
        During initialization it's making reduced form
    """

    def __init__(self, numerator=1, denominator=2):
        if not denominator:
            raise ZeroDivisionError("You can't div by 0")
        if isinstance(numerator, int) and isinstance(denominator, int):
            self.__numerator = numerator // gcd(numerator, denominator)
            self.__denominator = denominator // gcd(numerator, denominator)
        else:
            raise TypeError("Integers only")


    @property
    def numerator(self):
        """
        Getter for numerator
        """
        return self.__numerator

    @property
    def denominator(self):
        """
        Getter for denominator
        """
        return self.__denominator
    """
    Operators overloading
    """
    def __add__(self, second_item):
        """
        Adding two fractions
        Calculate the sum of first rational and second
        """
        if not isinstance(second_item, Rational):
            raise TypeError("only rational type")
        denom = self.denominator * second_item.denominator
        num = self.numerator * second_item.denominator + self.denominator * second_item.numerator
        return Rational(num, denom)

    def __sub__(self, second_item):
        """
            Subtracting two fractions
            Calculate the difference of first rational and second
        """
        if not isinstance(second_item, Rational):
            raise TypeError("only rational type")
        denom = self.denominator * second_item.denominator
        num = self.numerator * second_item.denominator - self.denominator * second_item.numerator
        return Rational(num, denom)

    def __mul__(self, second_item):
        """
            Multiplying two fractions
            Calculate the multiplication of first rational and second
        """
        if not isinstance(second_item, Rational):
            raise TypeError("only rational type")
        denom = self.denominator * second_item.denominator
        num = self.numerator * second_item.numerator
        return Rational(num, denom)

    def __truediv__(self, second_item):
        """
            Dividing two fractions
            Calculate the division of first rational and second
        """
        if not isinstance(second_item, Rational):
            raise TypeError("only rational type")
        denom = self.denominator * second_item.numerator
        num = self.numerator * second_item.denominator
        return Rational(num, denom)

    def __eq__(self, second_item):
        """
            Comparison of two fractions
            Checks for equality of 2 fractions
        """
        if not isinstance(second_item, Rational):
            raise TypeError("only rational type")
        first_num = self.numerator * second_item.denominator
        second_num = second_item.numerator * self.denominator
        return first_num == second_num

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def print_floating_point_format(self):
        """
        Return number in floating point number form
        """
        return self.numerator / self.denominator


def main():
    rational_first = Rational(2, 4)
    rational_sec = Rational(1, 4)
    rational_third = Rational(3, 6)
    print(rational_first)
    print(rational_first.print_floating_point_format())
    print("ADD:")
    print(rational_sec + rational_first)
    print("TRUEDIV:")
    print(rational_sec / rational_first)
    print("MUL:")
    print(rational_sec * rational_first)
    print("SUB:")
    print(rational_sec - rational_first)
    print("EQ:")
    print(rational_first == rational_sec)
    print(rational_first == rational_third)


main()
