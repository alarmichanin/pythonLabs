def gcd_recursive(num1, num2):
    if num2 == 0:
        return num1
    else:
        return gcd_recursive(num2, num1 % num2)
class Rational:
    def __init__(self,numerator=1,denominator=2):
        try:
            if isinstance(numerator,int) and isinstance(denominator,int):
                self.__numerator = numerator/gcd_recursive(numerator,denominator)
                self.__denominator = denominator/gcd_recursive(numerator,denominator)
                return None
        except:
            return None
    def print_normal_form(self):
        try:
            return print(self.__numerator,'/',self.__denominator)
        except:
            return None
    def print_floating_point_format(self):
        try:
            return print(self.__numerator/self.__denominator)
        except:
            return None
rational=Rational(5,10)
rational.print_normal_form()
rational.print_floating_point_format()
