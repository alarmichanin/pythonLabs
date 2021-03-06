from math import gcd


class Rational:
    def __init__(self, numerator=1, denominator=2):
            if not denominator:
                raise ZeroDivisionError("You can't div by 0")
            if isinstance(numerator, int) and isinstance(denominator, int):
                self.__numerator = numerator // gcd(numerator, denominator)
                self.__denominator = denominator // gcd(numerator, denominator)
            else:
                raise TypeError("Integers only")

    def __add__(self, second_item):
            if not isinstance(second_item, Rational):
                raise TypeError("only rational type")
            denom = self.__denominator * second_item.__denominator // gcd(self.__denominator, second_item.__denominator)
            num = denom // self.__denominator * self.__numerator + denom // second_item.__denominator * second_item.__numerator
            return Rational(num, denom)

    def __sub__(self, second_item):
            if not isinstance(second_item, Rational):
                raise TypeError("only rational type")
            denom = self.__denominator * second_item.__denominator // gcd(self.__denominator,
                                                                          second_item.__denominator)
            num = denom // self.__denominator * self.__numerator - denom // second_item.__denominator * second_item.__numerator
            return Rational(num, denom)

    def __mul__(self, second_item):
            if not isinstance(second_item, Rational):
                raise TypeError("only rational type")
            denom = self.__denominator * second_item.__denominator
            num = self.__numerator * second_item.__numerator
            return Rational(num, denom)

    def __truediv__(self, second_item):
            if not isinstance(second_item, Rational):
                raise TypeError("only rational type")
            denom = self.__denominator * second_item.__numerator
            num = self.__numerator * second_item.__denominator
            return Rational(num, denom)

    def print_normal_form(self):
            return f'{self.__numerator}/{self.__denominator}'

    def print_floating_point_format(self):
            return self.__numerator / self.__denominator


def main():
    try:
        rational_first = Rational(2, 4)
        print(rational_first.print_normal_form())
        print(rational_first.print_floating_point_format())
        rational_sec = Rational(1, 2)
        print("ADD:")
        print(rational_sec.__add__(rational_first).print_floating_point_format())
        print("TRUEDIV:")
        print(rational_sec.__truediv__(rational_first).print_floating_point_format())
        print("MUL:")
        print(rational_sec.__mul__(rational_first).print_floating_point_format())
        print("SUB:")
        print(rational_sec.__sub__(rational_first).print_floating_point_format())
    except:
        return None


main()
