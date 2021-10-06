import re
class Analyzer:
    def __init__(self, name_of_file="text.txt"):
        self.__name = name_of_file
        self.__content = ""

    def __read_file__(self):
        try:
            if not open(self.__name, "r"):
                raise FileNotFoundError("File not found")
            with open(self.__name, "r") as file:
                self.__content = file.read()
            return True
        except FileNotFoundError:
            return None

    def __count_words__(self):
        try:
            self.__read_file__()
            print(re.split(r'[\'\-\w]+', self.__content))
            return len(re.split(r'[\'\-\w]+', self.__content))-1
        except:
            return None

    def __count_symbols__(self):
        try:
            self.__read_file__()
            return len(self.__content)
        except:
            return None
    def __count_sentences__(self):
        try:
            self.__read_file__()
            return len(re.split(r'[.!?]+', self.__content))-1
        except:
            return None


obj1 = Analyzer()
print("Count of words: ", obj1.__count_words__())
print("Count of symbols: ", obj1.__count_symbols__())
print("Count of sentences: ", obj1.__count_sentences__())
