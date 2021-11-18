import json
import datetime

PIZZA_FILE = "pizzas.json"
INGREDIENTS_FILE = "ingredients.json"


class Menu:
    def __init__(self, pizzas, ingredients):
        self._pizzas = pizzas
        self._ingredients = ingredients

    def write_to_JSON(self):
        with open(PIZZA_FILE, "w") as write_file:
            json.dump(self._pizzas, write_file)
        with open(INGREDIENTS_FILE, "w") as write_file:
            json.dump(self._ingredients, write_file)


class Pizza:
    """
    Base class, that consist of functions:
    - Make pizza of the day (give opportunity to get pizza from json file)
    - Sum prices (to get price of the whole order: ingredients + pizzas)
    - We can check (if there are additional ingredients in the order
    and after that our function add or not add some data about it to the string of order)
    """
    def __init__(self, count, ingredients):
        if ingredients:
            with open(INGREDIENTS_FILE) as file:
                event = json.load(file)
                ings = [*event]
                if not all(tuple(x in ings for x in ingredients)):
                    raise ValueError("There is element which does not exist in the ingredient list")
                self._price_of_ingredients = 0
                for every in ingredients:
                    self._price_of_ingredients += event[every]
            self._ingredients = ingredients
        else:
            self._ingredients = 0
        self._count = count
        self._day = datetime.datetime.today().weekday()
        self._price_of_pizza = 0
        self._pizza_of_the_day = self.pizza_of_the_day_func()

    @property
    def pizza_of_the_day(self):
        return self._pizza_of_the_day

    @property
    def price_of_pizza(self):
        return self._price_of_pizza

    def pizza_of_the_day_func(self):
        with open(PIZZA_FILE) as file:
            event = json.load(file)
            pizzas = [*event]
            self._price_of_pizza = event[pizzas[self._day]]
        return pizzas[self._day]

    def order_price(self):
        if self._ingredients:
            return round(self._price_of_ingredients + self._price_of_pizza * self._count, 2)
        else:
            return self._price_of_pizza

    def if_ingredients(self):
        if self._ingredients:
            return f'\nAdditional ingredients: {",".join(self._ingredients)} - {self._price_of_ingredients}'
        else:
            return ''

    def __str__(self):
        return f'Pizza of the day: {self._pizza_of_the_day} - {self._price_of_pizza}{self.if_ingredients()}\nYour order price: {self.order_price()}\n'


class SpecialOrder(Pizza):
    """
    Pizza's class for special order (that isn't exist at default menu )
    If there are special order (not default pizza of the day), we can add it to the order
    (but first of all, we need give a name of special pizza + price of this pizza)
    """

    def __init__(self, title, price, count, add_ingredients):
        if not isinstance(title, str):
            raise TypeError("Pizza's name have to be string type only!")
        if not isinstance(price, float):
            raise TypeError("Pizza's price have to be float type only!")
        super().__init__(count, add_ingredients)
        self._pizza_of_the_day = title
        self._price_of_pizza = price

    @property
    def pizza_of_the_day(self):
        return self._pizza_of_the_day

    @property
    def price_of_pizza(self):
        return self._price_of_pizza


def order(count, is_default, add_ingredients=[], title="", price=0):
    """
    This function make a decision about which order we need to create (default with pizza of the day or special order)
    """
    if not isinstance(add_ingredients, list):
        raise TypeError("Ingredients have to be list type only!")
    if not isinstance(count, int):
        raise TypeError("count have to be int type only!")
    if not isinstance(is_default, bool):
        raise TypeError("is_default have to be bool type only!")
    if is_default:
        return Pizza(count, add_ingredients)
    else:
        return SpecialOrder(title, price, count, add_ingredients)


def main():
    pizzas = {
        'Margherita': 120,
        'Peperoni': 152,
        '4 Cheeses': 125,
        'Chicago': 237,
        'Americana': 203,
        'Marinara': 119,
        'Prosciutto': 171
    }
    ingredients = {
        'mushrooms': 15,
        'cheese': 35,
        'olives': 20,
        'lettuce': 10,
        'tomato': 15
    }
    Menu(pizzas, ingredients).write_to_JSON()
    ord1 = order(2, True, ['mushrooms', 'tomato'])
    ord2 = order(3, False, ['cheese', 'olives'], "Delicious", 99.99)
    ord3 = order(1, False, [], "Buenno", 100.99)
    print(ord1)
    print(ord2)
    print(ord3)


main()
