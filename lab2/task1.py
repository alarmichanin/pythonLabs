class Rectangle:
    def __init__(self, length=1, width=1):
        self.__length = length
        self.__width = width

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def set_length(self, length):
        if 0.0 <= length <= 20.0:
            self.__length = length
        else:
            raise ValueError

    def set_width(self, width):
        if 0.0 <= width <= 20.0:
            self.__width = width
        else:
            raise ValueError

    def perimeter(self):
        return (self.__width + self.__length) * 2

    def area(self):
        return self.__length * self.__width


def main():
    try:
        rectangle = Rectangle()
        rectangle.set_length(10)
        rectangle.set_width(10.2)
        print(rectangle.area(), rectangle.perimeter())
    except:
        return None


main()
