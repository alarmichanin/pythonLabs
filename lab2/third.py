from statistics import mean
import uuid


class Student:
    """Class consists of array and 2 methods
    In initialization we can check that everything is ok and after that, get average score of each student
    Also in the end we make some overloading of standard method str"""
    __slots__ = ("_name", "_surname", "_record_book_number", "__grades", "_average")
    students = []

    def __init__(self, name, surname, grades):
        if not isinstance(grades, list):
            raise TypeError("Grades have to be list type")
        if f"{name} {surname}" in Student.students or f"{surname} {name}" in Student.students:
            raise ValueError("This student is already exist")
        if not all(isinstance(elem, int) for elem in grades):
            raise TypeError("Grades can be int type only")
        self._name = name
        self._surname = surname
        self._record_book_number = uuid.uuid4()
        self.__grades = grades
        self._average = self.average(grades)
        Student.students.append(f"{name} {surname}")

    def average(self, marks):
        return mean(marks)

    def __str__(self):
        return f"{self._name} {self._surname} ({self._record_book_number}): {self._average}"


MAX_STUDENTS = 20


class Group:
    """In class Group we make some method success that give us list of the top 5 students in the group
    Also we made check that count of students can't be more than 20 """

    def __init__(self, students):
        if not isinstance(students, list):
            raise TypeError("Students have to be a list type")
        if len(students) > MAX_STUDENTS:
            raise ValueError("Count of students have to be less than 20")
        if not all(isinstance(student, Student) for student in students):
            raise TypeError("Student can be Student type only")
        self.__students = students

    def success(self):
        top = [
            successful_student
            for successful_student in sorted(self.__students, reverse=True,
                                             key=lambda x: x._average)[:5]
        ]
        return top


student1 = Student("Yaroslav", "Dyhanov", grades=[5, 5, 4, 4, 5, 5, 4, 5])
student2 = Student("Vitaly", "Kovalev", grades=[5, 5, 4, 4, 4, 5, 5, 5])
student3 = Student("Maxim", "Vashchenko", grades=[3, 3, 3, 5, 5, 3, 3, 5])
student4 = Student("Denys", "Zahariya", grades=[5, 5, 4, 3, 5, 3, 4, 5])
student5 = Student("Arseniy", "Metz", grades=[5, 5, 4, 4, 5, 5, 4, 5])
student6 = Student("Maxim", "Klapatyuk", grades=[5, 5, 1, 4, 5, 5, 5, 5])
student7 = Student("Pavlo", "Nedashkivsky", grades=[5, 5, 5, 5, 5, 5, 4, 5])
group = [student1, student2, student3, student4, student5, student6, student7]
ti_01 = Group(group)
for every in ti_01.success():
    print(every)
