class Product:
    def __init__(self, price=0, description="smth here", h=10, w=10, l=10):
        self.price = price
        self.__description = description
        self.__dimensions = [h, w, l]


class Customer:
    def __init__(self, surname="Musk", name="Elon", patronymic="Manovich", phone="880055553535"):
        self.__surname = surname
        self.__name = name
        self.__patronymic = patronymic
        self.phone = phone


class Order(Product, Customer):
    __orders = {}

    def __init__(self, price=10, description="iPad", h=120, w=40, l=20, surname="Musk", name="Elon",
                 patronymic="Manovich", phone="880055553535"):
        Product.__init__(self, price, description, h, w, l)
        Customer.__init__(self, surname, name, patronymic, phone)
        if self.__orders.get(phone):
            self.__orders[phone].append(self)
        else:
            self.__orders[phone] = [self]

    def __total_value__(self):
        total = 0
        for order in self.__orders[self.phone]:
            total += order.price
        return total


def main():
    order1 = Order(100, 'iPhone', 100, 2, 10, 'Tkachenko', 'Roman', 'Olegovich', '0997435612')
    order2 = Order(120, 'iMac', 100, 15, 10, 'Tkachenko', 'Roman', 'Olegovich', '0997435612')
    order3 = Order()
    print(order1.__total_value__())
    print(order2.__total_value__())
    print(order3.__total_value__())


main()
