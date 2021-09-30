class Rectangle:
    def __init__(self):
        self.__length = 1
        self.__width = 1
    def get_length(self):
        return self.__length
    def get_width(self):
        return self.__width
    def set_length(self,length):
        try:
            if 0.0<=length<=20.0:
                self.__length=length
                return True
        except:
            return None

    def set_width(self,width):
        try:
            if 0.0<=width<=20.0:
                self.__width=width
                return True
        except:
            return None
    def perimeter(self):
        return (self.__width+self.__length)*2
    def area(self):
        return self.__length*self.__width
rectangle = Rectangle()
rectangle.set_length('asd')
rectangle.set_width(10.2)
print(rectangle.area(),rectangle.perimeter())
