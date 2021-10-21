class BinaryTree:
    """General class BinaryTree consists of 3 methods (__init__, insert,get_cost)"""
    __slots__ = ("_barcode", "_unit_price", "left", "right")

    def __init__(self, barcode, unit_price):
        """We check there barcode and price, after that initialize base values"""
        if barcode < 0:
            raise ValueError("Barcode must consist of numbers >= 0")
        if unit_price <= 0:
            raise ValueError("Unit must cost more than nothing")
        self.left = None
        self.right = None
        self._barcode = barcode
        self._unit_price = unit_price

    def insert(self, barcode, unit_price):
        """This method give us an opportunity to insert new elements in BinaryTree with sort
         from the start"""
        if barcode == self._barcode:
            raise ValueError("This barcode already exists")
        if barcode < self._barcode:
            if self.left is None:
                self.left = BinaryTree(barcode, unit_price)
            else:
                self.left.insert(barcode, unit_price)
        elif barcode > self._barcode:
            if self.right is None:
                self.right = BinaryTree(barcode, unit_price)
            else:
                self.right.insert(barcode, unit_price)

    def get_cost(self, barcode):
        """Final method, that help us to get price of an order (which consists of number of product
        and barcode)"""
        if barcode < self._barcode:
            if self.left is None:
                return f"{barcode} isn't available"
            else:
                return self.left.get_cost(barcode)
        elif barcode > self._barcode:
            if self.right is None:
                return f"{barcode} isn't available"
            else:
                return self.right.get_cost(barcode)
        else:
            return self._unit_price


def main():
    root = BinaryTree(232, 7)
    root.insert(212, 15)
    root.insert(289, 3)
    root.insert(231, 10)
    root.insert(290, 11)
    root.insert(277, 90)
    root.insert(200, 4)
    root.insert(233, 43)
    root.insert(298, 32)
    root.insert(213, 1)
    try:
        code_product = int(input('Enter your barcode: '))
        quantity = int(input("Enter number of product: "))
        price = root.get_cost(code_product)
        if isinstance(price, int):
            print(price * quantity)
    except ValueError:
        return None


main()
