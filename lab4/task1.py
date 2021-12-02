from math import gcd
import operator


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

    @numerator.setter
    def numerator(self, other):
        """
        Setter for numerator
        """
        if isinstance(other, int):
            self.__numerator = other
        else:
            raise TypeError("Numerator has to be integer type only")

    @property
    def denominator(self):
        """
        Getter for denominator
        """
        return self.__denominator

    @denominator.setter
    def denominator(self, other):
        """
        Setter for denominator
        """
        if isinstance(other, int):
            self.__denominator = other
        else:
            raise TypeError("Denominator has to be integer type only")

    def reduction(self):
        n = gcd(self.numerator, self.denominator)
        self.numerator //= n
        self.denominator //= n

    """
    Operators overloading
    """

    def __wrap__(self, other, oper):
        """
        Wrapper for "+" and "-" operators
        (Method that get an operator for overloading and overloads it)
        """
        if isinstance(other, Rational):
            self.numerator = oper(self.numerator * other.denominator, self.denominator * other.numerator)
            self.denominator = self.denominator * other.denominator
            self.reduction()
            return self
        if isinstance(other, int):
            self.numerator = oper(self.numerator, other * self.denominator)
            self.reduction()
            return self
        raise TypeError("Rational and int types only")

    def __add__(self, other):
        """
        Adding two fractions
        Calculate the sum of first rational and second
        """
        return self.__wrap__(other, operator.add)

    def __sub__(self, other):
        """
            Subtracting two fractions
            Calculate the difference of first rational and second
        """
        return self.__wrap__(other, operator.sub)

    def __mul__(self, other):
        """
            Multiplying two fractions
            Calculate the multiplication of first rational and second
        """
        if isinstance(other, Rational):
            self.numerator = self.numerator * other.numerator
            self.denominator = self.denominator * other.denominator
            self.reduction()
            return self
        if isinstance(other, int):
            self.numerator = self.numerator * other
            self.reduction()
            return self
        raise TypeError("only rational and int types")

    def __truediv__(self, other):
        """
            Dividing two fractions
            Calculate the division of first rational and second
        """
        if isinstance(other, Rational):
            self.numerator = self.numerator * other.denominator
            self.denominator = self.denominator * other.numerator
            self.reduction()
            return self
        if isinstance(other, int):
            self.denominator = self.denominator * other.numerator
            self.reduction()
            return self
        raise TypeError("only rational and int types")

    def __iadd__(self, other):
        """
        Overloading "+=" operator
        """
        return self.__wrap__(other, operator.add)

    def __isub__(self, other):
        """
        Overloading "-=" operator
        """
        return self.__wrap__(other, operator.sub)

    def __imul__(self, other):
        """
        Overloading "*=" operator
        """
        if isinstance(other, Rational):
            self.numerator = self.numerator * other.numerator
            self.denominator = self.denominator * other.denominator
            self.reduction()
            return self
        if isinstance(other, int):
            self.numerator = self.numerator * other
            self.reduction()
            return self
        raise TypeError("only rational and int types")

    def __itruediv__(self, other):
        """
        Overloading "/=" operator
        """
        if isinstance(other, Rational):
            self.numerator = self.numerator * other.denominator
            self.denominator = self.denominator * other.numerator
            self.reduction()
            return self
        if isinstance(other, int):
            self.denominator = self.denominator * other.numerator
            self.reduction()
            return self
        raise TypeError("only rational and int types")

    def __cmp__(self, other, oper):
        """
        Method that get an operator for overloading and overloads it
        """
        if isinstance(other, Rational):
            return oper(self.numerator * other.denominator, self.denominator * other.numerator)
        if isinstance(other, int):
            return oper(self.numerator, self.denominator * other)
        return TypeError("For comparing Rational and int types only")

    def __eq__(self, other):
        """
            Comparison of two fractions
            Checks for equality of 2 fractions
        """
        return self.__cmp__(other, operator.eq)

    def __gt__(self, other):
        """
        Comparison of two fractions
        Checks for greater one among 2 fractions
        """
        return self.__cmp__(other, operator.gt)

    def __ge__(self, other):
        """
        Comparison of two fractions
        Checks for greater and equal one among 2 fractions
        """
        return self.__cmp__(other, operator.gt)

    def __lt__(self, other):
        """
        Comparison of two fractions
        Checks for less one among 2 fractions
        """
        return self.__cmp__(other, operator.lt)

    def __le__(self, other):
        """
        Comparison of two fractions
        Checks for less and equal one among 2 fractions
        """
        return self.__cmp__(other, operator.le)

    def __str__(self):
        """
        Overloading str operator
        """
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
