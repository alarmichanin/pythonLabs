DAYS_IN_MONTH = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


class Calendar:
    def __init__(self, day, month, year):
        if not isinstance(year, int):
            raise TypeError("Year has to be integer type only")
        if not isinstance(month, int):
            raise TypeError("Month has to be integer type only")
        if not 0 < month < 13:
            raise ValueError("Day has to be in scope (1,12)")
        if not isinstance(day, int):
            raise TypeError("Day has to be integer type only")
        if month == 2:
            if year % 4 == 0:
                if not 0 < day < 30:
                    raise ValueError("It is a leap year with a maximum of 29 days in February")
            else:
                if not 0 < day < 29:
                    raise ValueError("It isn't a leap year, so maximum of days in February are 28")
        else:
            if not 0 < day <= DAYS_IN_MONTH[month - 1]:
                raise ValueError("Day has to be in scope (1,31)")
        self.__day = day
        self.__month = month
        self.__year = year

    @property
    def day(self):
        return self.__day

    @property
    def month(self):
        return self.__month

    @property
    def year(self):
        return self.__year

    def __str__(self):
        return f'Day: {self.day}\nMonth: {self.month}\nYear: {self.year}'

    def __iadd__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError("Second item have to be Calendar type only")
    #     TODO: += and -= operators 

    def __eq__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError("Second item have to be Calendar type only")
        if self.year == other.year and self.month == other.month and self.day == other.day:
            return True
        return False

    def __ne__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError("Second item have to be Calendar type only")
        if self.year != other.year or self.month != other.month or self.day != other.day:
            return True
        return False

    def __gt__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError("Second item have to be Calendar type only")
        if self.year > other.year:
            return True
        if self.year == other.year:
            if self.month > other.month:
                return True
            if self.month == other.month:
                if self.day > other.day:
                    return True
        return False

    def __ge__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError("Second item have to be Calendar type only")
        if self.year > other.year:
            return True
        if self.year == other.year:
            if self.month > other.month:
                return True
            if self.month == other.month:
                if self.day >= other.day:
                    return True
        return False

    def __lt__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError("Second item have to be Calendar type only")
        if self.year < other.year:
            return True
        if self.year == other.year:
            if self.month < other.month:
                return True
            if self.month == other.month:
                if self.day < other.day:
                    return True
        return False

    def __le__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError("Second item have to be Calendar type only")
        if self.year < other.year:
            return True
        if self.year == other.year:
            if self.month < other.month:
                return True
            if self.month == other.month:
                if self.day <= other.day:
                    return True
        return False


def main():
    a = Calendar(29, 2, 2000)
    b = Calendar(29, 2, 2000)
    print(a <= b)


main()
