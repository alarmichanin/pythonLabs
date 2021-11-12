import uuid
import json
import datetime
from discounts import DISCOUNT_ADVANCED, DISCOUNT_LATE, DISCOUNT_STUDENT


class ITEvent:
    """class for making some It event """

    def __init__(self, price, day, month, year, num_of_tickets):
        if isinstance(price, (float, int)):
            self._price = price
        else:
            raise TypeError("Price have to be float type only!")
        if isinstance(num_of_tickets, int):
            self._num_of_tickets = num_of_tickets
        else:
            raise TypeError("Number of tickets have to be integer type only!")
        self._date = datetime.date(year, month, day)

    def write_to_JSON(self):
        """method that write data to JSON file"""
        event_dict = {"id": str(uuid.uuid4()), "price": self._price, "number": self._num_of_tickets,
                      "date": str(self._date)}
        with open("ITevent.json", "w") as write_file:
            json.dump(event_dict, write_file)


class RegularTicket:
    """Base ticket class"""

    def __init__(self):
        self._id = uuid.uuid4()
        with open("ITevent.json") as file:
            event = json.load(file)
            self._price = event["price"]
        self._type = "Regular ticket"

    @property
    def id(self):
        return self._id

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if isinstance(price, float):
            self._price = price
        else:
            raise TypeError("Price have to be float type only!")

    def __str__(self):
        return f"Type: {self._type}\nID: {self._id}\nPrice: {self._price}"


class AdvanceTicket(RegularTicket):
    """Advance ticket class, that have 40% discount on the basic ticket price"""

    def __init__(self):
        super().__init__()
        self._type = "Advance ticket"

    @property
    def price(self):
        return self._price - (self._price * DISCOUNT_ADVANCED) / 100


class LateTicket(RegularTicket):
    """Late ticket class, that have 10% discount on the basic ticket price"""

    def __init__(self):
        super().__init__()
        self._type = "Late ticket"

    @property
    def price(self):
        return self._price - (self._price * DISCOUNT_LATE) / 100


class StudentTicket(RegularTicket):
    """Student ticket class, that have 50% discount on the basic ticket price"""

    def __init__(self):
        super().__init__()
        self._type = "Student ticket"

    @property
    def price(self):
        return self._price - (self._price * DISCOUNT_STUDENT) / 100


class Client:
    """Client class that describe customer that order the ticket """

    def __init__(self, name, surname, is_student):
        if not isinstance(name, str):
            raise TypeError("Name have to be string type only!")
        if not isinstance(surname, str):
            raise TypeError("Surname have to be string type only!")
        if not isinstance(is_student, bool):
            raise TypeError("is_student have to be boolean type only")
        self.__name = name
        self.__surname = surname
        self.__is_student = is_student

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise TypeError("Name have to be string type only!")

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if isinstance(surname, str):
            self.__surname = surname
        else:
            raise TypeError("Surname have to be string type only!")

    @property
    def is_student(self):
        return self.__is_student

    @is_student.setter
    def is_student(self, is_student):
        if isinstance(is_student, bool):
            self.__is_student = is_student
        else:
            raise TypeError("is_student have to be boolean type only!")


class Order:
    """Order class consist of the methods that allow to get full information about the ticket"""

    def __init__(self, client):
        if isinstance(client, Client):
            self.__client = client
        else:
            raise TypeError("Client have to be object's Client type!")

    @staticmethod
    def days_to_event():
        """method to count difference in days between date of event and purchase date"""
        today = datetime.date.today()
        with open("ITevent.json") as file:
            event = json.load(file)
            date_of_event = datetime.datetime.strptime(event["date"], "%Y-%m-%d").date()
        diff = (date_of_event - today).days
        return diff

    def choose_ticket(self, days):
        """method to get right type of ticket"""
        if self.__client.is_student:
            return StudentTicket()
        if isinstance(days, int) and days > 0:
            if days >= 60:
                return AdvanceTicket()
            elif days in range(11):
                return LateTicket()
            else:
                return RegularTicket()
        else:
            raise TypeError("Difference in date have to be integer type only and > 0 (check your dates)!")

    @staticmethod
    def get_ticket_price(ticket_type):
        """method to get price of ticket"""
        if isinstance(ticket_type, (RegularTicket, StudentTicket, AdvanceTicket, LateTicket)):
            return ticket_type._price
        else:
            raise TypeError("ticket_type have to be one of the type of ticket")

    def ticket_maker(self, ticket_type, days_to_event):
        """method to make dictionary with full information about ticket"""
        ticket_dict = {str(ticket_type._id): {}}
        ticket_dict[str(ticket_type._id)]["name"] = self.__client.name
        ticket_dict[str(ticket_type._id)]["surname"] = self.__client.surname
        ticket_dict[str(ticket_type._id)]["is_student"] = self.__client.is_student
        ticket_dict[str(ticket_type._id)]["type_of_ticket"] = ticket_type._type
        ticket_dict[str(ticket_type._id)]["price"] = ticket_type._price
        ticket_dict[str(ticket_type._id)]["purchase_date"] = str(datetime.date.today())
        with open("ITevent.json") as file:
            event = json.load(file)
            date_of_event = datetime.datetime.strptime(event["date"], "%Y-%m-%d").date()
        ticket_dict[str(ticket_type._id)]["event_date"] = str(date_of_event)
        ticket_dict[str(ticket_type._id)]["days_to_event"] = days_to_event
        return ticket_dict

    def buy(self):
        """method to buy a ticket, allows to make some note in json file about order, and control
        if there are enough number of tickets """
        days = self.days_to_event()
        ticket_type = self.choose_ticket(days)
        with open("ITevent.json") as file:
            content = json.load(file)
            ticket_num = content["number"]
        with open("orders.json") as orders:
            tmp = json.load(orders)
            if len(tmp) >= ticket_num:
                raise ValueError("Ticket ran out of stock")
            tmp.append(self.ticket_maker(ticket_type, days))
        with open("orders.json", "w") as file:
            json.dump(tmp, file)

    def __str__(self):
        days = self.days_to_event()
        ticket_type = self.choose_ticket(days)
        ticket_info = self.ticket_maker(ticket_type, days)
        dict_items = ticket_info[str(ticket_type._id)].items()
        info = "Ticket info:"
        for every in dict_items:
            info += "\n"
            for each in every:
                info += str(each) + " "
        return info


def main():
    google_ev = ITEvent(500, 18, 11, 2021, 15)
    google_ev.write_to_JSON()
    client = Client("Roman", "Tkachenko", False)
    ord = Order(client)
    print(ord)
    ord.buy()
    # to get price of ticket (direct request)
    # print(ord.get_ticket_price(ord.choose_ticket(ord.days_to_event())))


main()
