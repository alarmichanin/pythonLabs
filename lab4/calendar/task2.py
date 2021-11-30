DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


class ChangeTime:
    def __init__(self, days=0, months=0, years=0):
        if not isinstance(days, int):
            raise TypeError("Days have to be integer type only")
        if not isinstance(months, int):
            raise TypeError("Months have to be integer type only")
        if not isinstance(years, int):
            raise TypeError("Years have to be integer type only")
        if (days or months or years) < 0:
            raise ValueError("Value has to be greater then 0")
        self.__days = days
        self.__months = months
        self.__years = years

    @property
    def days(self):
        return self.__days

    @days.setter
    def days(self, days: int):
        if isinstance(days, int):
            self.__days = days
        else:
            raise TypeError("Days has to be integer type only")

    @property
    def months(self):
        return self.__months

    @property
    def years(self):
        return self.__years


class Calendar:
    def __init__(self, day: int, month: int, year: int):
        if not isinstance(year, int):
            raise TypeError("Year has to be integer type only")
        if not isinstance(month, int):
            raise TypeError("Month has to be integer type only")
        if not 0 < month < 13:
            raise ValueError("Day has to be in scope (1,12)")
        if not isinstance(day, int):
            raise TypeError("Day has to be integer type only")
        if month == 2:
            if not year % 4:
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

    @day.setter
    def day(self, day):
        if isinstance(day, int):
            self.__day = day
        else:
            raise TypeError("Day has to be integer type only")

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month):
        if isinstance(month, int):
            self.__month = month
        else:
            raise TypeError("Month has to be integer type only")

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if isinstance(year, int):
            self.__year = year
        else:
            raise TypeError("Year has to be integer type only")

    def __str__(self):
        return f'Day: {self.day}\nMonth: {self.month}\nYear: {self.year}'

    def __iadd__(self, other: ChangeTime):
        if not isinstance(other, ChangeTime):
            raise TypeError("Second item have to be changeTime type only")
        self.year += other.years
        if self.month + other.months > 12:
            self.year += (self.month + other.months) // 12
            self.month = (self.month + other.months) % 12
        else:
            self.month += other.months
        while other.days > 0:
            if not self.year % 4:
                DAYS_IN_MONTH[1] = 29
            else:
                DAYS_IN_MONTH[1] = 28
            if self.day + other.days - DAYS_IN_MONTH[self.month - 1] > 0:
                other.days = self.day + other.days - DAYS_IN_MONTH[self.month - 1]
                self.day = 0
                if not self.month + 1 > 12:
                    self.month += 1
                else:
                    self.year += 1
                    self.month = 1
            else:
                self.day += other.days
                other.days = 0
            if self.year % 4 and self.month == 2 and self.day > 28:
                self.month += 1
                self.day = self.day - 28

        return Calendar(self.day, self.month, self.year)

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
    a = Calendar(28, 2, 2003)
    b = Calendar(29, 2, 2000)
    c = ChangeTime(50, 12, 0)
    a += c
    print(a)


main()
