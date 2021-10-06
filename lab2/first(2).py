class Product:
    def __init__(self, price=0, description="smth here", h=10, w=10, l=10):
        self.__price = price
        self.__description = description
        self.__dimensions = [h, w, l]

    def get_price(self):
        return self.__price


class Customer:
    def __init__(self, surname="Musk", name="Elon", patronymic="patronymic", phone="880055553535"):
        self.__surname = surname
        self.__name = name
        self.__patronymic = patronymic
        self.__phone = phone
    def get_print(self):
        return f'{self.__name} {self.__surname}'


class Order:
    def __init__(self, product, customer):
        self.__customer = customer
        self.__products = product
        self.__total = self.__counting__()

    def __counting__(self):
        total = 0
        for item in self.__products:
            total += item.get_price()
        return total


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
        print(f'{customer1.get_print()} total sum: {order1.__counting__()}')
        print(f'{customer2.get_print()} total sum: {order2.__counting__()}')
    except:
        return None


main()
