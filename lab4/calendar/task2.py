DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def leap_year(year):
    """
    function for checking if there is leap year
    """
    return not year % 4 and year % 100 or not year % 400


class ChangeTime:
    """
    Class consists of three fields:
    There are checking on correct input (every value has to be greater than 0)
    - days
    - months
    - years
    It gives us the opportunity to make an object for addition with the Calendar class
    """

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
        """
        Getter for days
        """
        return self.__days

    @days.setter
    def days(self, days: int):
        """
        Setter for days
        """
        if isinstance(days, int):
            self.__days = days
        else:
            raise TypeError("Days has to be integer type only")

    @property
    def months(self):
        """
        Getter for months
        """
        return self.__months

    @property
    def years(self):
        """
        Getter for years
        """
        return self.__years

    def __str__(self):
        """
        Overloading str operator
        """
        return f'Days: {self.days}\nMonths: {self.months}\nYears: {self.years}'


class Calendar:
    """
    Class consists of three fields:
    - days      (there is checking on correctly day, depends on leap year )
    - months    (there is checking on correctly month, depends on value greater than 0 and less than 13)
    - years     (there is checking on correctly year, depends on value greater than 0)
    """

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
            if leap_year(year):
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
        """
        Getter for day
        """
        return self.__day

    @day.setter
    def day(self, day):
        """
        Setter for day
        """
        if isinstance(day, int):
            self.__day = day
        else:
            raise TypeError("Day has to be integer type only")

    @property
    def month(self):
        """
        Getter for month
        """
        return self.__month

    @month.setter
    def month(self, month):
        """
        Setter for month
        """
        if isinstance(month, int):
            self.__month = month
        else:
            raise TypeError("Month has to be integer type only")

    @property
    def year(self):
        """
        Getter for year
        """
        return self.__year

    @year.setter
    def year(self, year):
        """
        Setter for year
        """
        if isinstance(year, int):
            self.__year = year
        else:
            raise TypeError("Year has to be integer type only")

    def __str__(self):
        """
        Overloading str operator
        """
        return f'Day: {self.day}\nMonth: {self.month}\nYear: {self.year}'

    def __iadd__(self, other: ChangeTime):
        """
        Overloading of += operator, for adding some days,months,years to the some date
        """
        if not isinstance(other, ChangeTime):
            raise TypeError("Second item have to be changeTime type only")
        self.year += other.years
        if self.month + other.months > 12:
            self.year += (self.month + other.months) // 12
            if leap_year(self.__year) and self.month == 2 and self.day > 28:
                self.month = (self.month + other.months) % 12 + 1
                self.day = self.day - 28
            else:
                if leap_year(self.__year):
                    DAYS_IN_MONTH[1] = 29
                else:
                    DAYS_IN_MONTH[1] = 28
                self.month = (self.month + other.months) % 12
                self.day = DAYS_IN_MONTH[self.month - 1]
        else:
            self.month += other.months
        while other.days > 0:
            if leap_year(self.__year):
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
            if leap_year(self.__year) and self.month == 2 and self.day > 28:
                self.month += 1
                self.day = self.day - 28
        return Calendar(self.day, self.month, self.year)

    def __isub__(self, other):
        """
        Overloading of -= operator, for subtraction some days,months,years to the some date
        """
        if not isinstance(other, ChangeTime):
            raise TypeError("Second item have to be changeTime type only")
        self.year -= other.years
        if self.month - other.months <= 0:
            if other.months < 12:
                self.year -= 1
                self.month = 12 - (other.months - self.month)
            else:
                self.year -= other.months // 12
                if self.month - other.months % 12 <= 0:
                    self.month = 12 - other.months % 12 + self.month
                    self.year -= 1
                    if leap_year(self.__year) and self.month == 2 and self.day > 28:
                        self.month += 1
                        self.day = self.day - 28
                else:
                    if other.months % 12:
                        self.month -= other.months % 12
                    else:
                        if leap_year(self.__year):
                            DAYS_IN_MONTH[1] = 29
                        else:
                            DAYS_IN_MONTH[1] = 28
                    if leap_year(self.__year) and self.month == 2 and self.day > 28:
                        self.month += 1
                        self.day = self.day - 28
        else:
            self.month -= other.months
        while other.days > 0:
            if leap_year(self.__year):
                DAYS_IN_MONTH[1] = 29
            else:
                DAYS_IN_MONTH[1] = 28
            if self.day - other.days < 0:
                other.days -= self.day
                if self.month - 1 < 1:
                    self.year -= 1
                    self.month = 12
                else:
                    self.month -= 1
                self.day = DAYS_IN_MONTH[self.month - 1]
            else:
                if self.day - other.days:
                    self.day -= other.days
                else:
                    if self.month - 1 <= 0:
                        self.month = 12
                        self.year -= 1
                    else:
                        self.month -= 1
                    self.day = DAYS_IN_MONTH[self.month - 1]
                other.days = 0
        return Calendar(self.day, self.month, self.year)

    def __eq__(self, other):
        """
        Overloading of == operator, for comparing two dates
        """
        if not isinstance(other, Calendar):
            raise TypeError("Second item have to be Calendar type only")
        if self.year == other.year and self.month == other.month and self.day == other.day:
            return True
        return False

    def __ne__(self, other):
        """
        Overloading of != operator, for comparing two dates
        """
        if not isinstance(other, Calendar):
            raise TypeError("Second item have to be Calendar type only")
        if self.year != other.year or self.month != other.month or self.day != other.day:
            return True
        return False

    def __gt__(self, other):
        """
        Overloading of > operator, for comparing two dates
        """
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
        """
        Overloading of >= operator, for comparing two dates
        """
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
        """
        Overloading of < operator, for comparing two dates
        """
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
        """
        Overloading of <= operator, for comparing two dates
        """
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
    first_date = Calendar(30, 12, 2003)
    second_date = Calendar(29, 2, 2000)
    time_for_plus = ChangeTime(0, 12, 0)
    time_for_minus = ChangeTime(31, 12, 0)
    first_date -= time_for_minus
    second_date += time_for_plus
    print(first_date)
    print(second_date)


main()
