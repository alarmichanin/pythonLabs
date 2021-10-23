import re


class Analyzer:
    __slots__ = ("__name", "__content")

    def __init__(self, name_of_file="text.txt"):
        if not isinstance(name_of_file, str):
            raise TypeError("File name have to be in str type")
        self.__name = name_of_file
        self.__content = ""

    def __read_file__(self):
        try:
            if not self.__content:
                with open(self.__name, "r") as file:
                    self.__content += file.read()
        except IOError:
            return False

    def __count_words__(self):
        self.__read_file__()
        return len(re.split(r'[\'\-\w]+', self.__content)) - 1

    def __count_symbols__(self):
        self.__read_file__()
        return len(self.__content)

    def __count_sentences__(self):
        self.__read_file__()
        return len(re.split(r'[.!?]+', self.__content)) - 1


obj1 = Analyzer()
print("Count of words: ", obj1.__count_words__())
print("Count of symbols: ", obj1.__count_symbols__())
print("Count of sentences: ", obj1.__count_sentences__())
