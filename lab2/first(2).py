class Product:
    __slots__ = ("__price", "__description", "__dimensions")

    def __init__(self, price=0, description="smth here", h=10, w=10, l=10):
        self.__description = description
        if price < 0 or h < 0 or w < 0 or l < 0:
            raise ValueError("Dimensions or price can\'t be lower than 0")
        if not isinstance(price, (int, float)) or isinstance((h, w, l), int):
            raise TypeError("Wrong type")
        self.__price = price
        self.__dimensions = [h, w, l]

    def get_price(self):
        return self.__price


class Customer:
    __slots__ = ("__surname", "__name", "__patronymic", "__phone")

    def __init__(self, surname="Musk", name="Elon", patronymic="patronymic", phone="880055553535"):
        self.__surname = surname
        self.__name = name
        self.__patronymic = patronymic
        self.__phone = phone

    def __str__(self):
        return f'{self.__name} {self.__surname} {self.__patronymic}'


class Order:
    __slots__ = ("__customer", "__products", "__total")

    def __init__(self, product, customer):
        if not isinstance(customer, Customer):
            raise TypeError("Only Customer type available for Customer")
        self.__customer = customer
        for elem in product:
            if not isinstance(elem, Product):
                raise TypeError("Only Product type available for Product")
        self.__products = product
        self.__total = self.__counting__()

    def __counting__(self):
        total = 0
        for item in self.__products:
            total += item.get_price()
        return total

    def __str__(self):
        return f"{self.__customer} total sum: {self.__counting__()}"


def main():
    try:
        product1 = Product(500, "iPhone X", 20, 140, 100)
        product2 = Product(540, "iPhone XR", 18, 150, 110)
        product3 = Product(640, "iPhone 12", 14, 170, 100)
        product4 = Product(700, "iPhone 12 Pro", 13, 175, 100)
        customer1 = Customer("Tkachenko", "Roman", "Olegovich", "0997435293")
        customer2 = Customer("Denus", "Ilya", "Andriyovich", "0942659504")
        order1 = Order([product1, product4, product2], customer1)
        order2 = Order([product3, product1], customer2)
        print(order1)
        print(order2)
    except:
        return None


main()
