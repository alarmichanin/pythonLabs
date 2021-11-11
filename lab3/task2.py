pizza = {
    1: 'Margherita',
    2: 'Peperoni',
    3: '4 Cheeses',
    4: 'Chicago',
    5: 'Americana',
    6: 'Marinara',
    7: 'Prosciutto'
}

price = {
    'Margherita': 120,
    'Peperoni': 152,
    '4 Cheeses': 125,
    'Chicago': 237,
    'Americana': 203,
    'Marinara': 119,
    'Prosciutto': 171
}


class Pizza:
    def __init__(self, day):
        if isinstance(day, int):
            self.day = day
        else:
            raise TypeError("Day have to be integer type")
        self.total = 0

    def order_pizza(self, name_of_pizza, potential_products):
        if not isinstance(name_of_pizza, str):
            raise TypeError("name_of_pizza have to be string type only")
        if not isinstance(potential_products, list):
            raise TypeError("potential_products have to be list type only")
        if name_of_pizza not in price:
            raise ValueError("Look at pizza list")
        self.total += price[name_of_pizza]
        total_products = str(potential_products)
        return f'{name_of_pizza} added to the order!\nAdded products:{total_products}\nPrice:{price[name_of_pizza]}\nTotal price:{self.total}'

    def pizza_of_the_day(self):
        if self.day < 1 or self.day > 7:
            raise ValueError("Unreal day!")
        return pizza[self.day]

    def order_price(self):
        return self.total


ord = Pizza(7)
print(ord.order_pizza('4 Cheeses', ['Mushrooms', 'Meet']))
print(ord.order_pizza('Chicago', ['Cheese']))
print(ord.order_price())
print(ord.pizza_of_the_day())
