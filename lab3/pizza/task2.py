import json
import datetime


class Menu:
    def __init__(self, pizzas, ingredients):
        self._pizzas = pizzas
        self._ingredients = ingredients

    def write_to_JSON(self):
        with open("pizzas.json", "w") as write_file:
            json.dump(self._pizzas, write_file)
        with open("ingredients.json", "w") as write_file:
            json.dump(self._ingredients, write_file)


class Pizza:
    def __init__(self, ingredients=[]):
        if not isinstance(ingredients, list):
            raise TypeError("Ingredients have to be list type only!")
        if ingredients:
            with open("ingredients.json") as file:
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
        self._day = datetime.datetime.today().weekday()
        self._price_of_pizza = 0
        self._pizza_of_the_day = self.pizza_of_the_day()

    def pizza_of_the_day(self):
        with open("pizzas.json") as file:
            event = json.load(file)
            pizzas = [*event]
            self._price_of_pizza = event[pizzas[self._day]]
        return pizzas[self._day]

    def order_price(self):
        if self._ingredients:
            return self._price_of_ingredients + self._price_of_pizza
        else:
            return self._price_of_pizza

    def if_ingredients(self):
        if self._ingredients:
            return f'\nAdditional ingredients: {",".join(self._ingredients)} - {self._price_of_ingredients}'
        else:
            return ''

    def __str__(self):
        return f'Pizza of the day: {self._pizza_of_the_day} - {self._price_of_pizza}{self.if_ingredients()}\nYour order price: {self.order_price()}\n'


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
    ord1 = Pizza(['mushrooms', 'tomato'])
    ord2 = Pizza()
    print(ord1)
    print(ord2)


main()
