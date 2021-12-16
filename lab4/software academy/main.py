from interfaces import ICourse, ILocalCourse, IOffsiteCourse, ITeacher, ICourseFactory
import json

COURSES = "courses.json"
TEACHERS = "teachers.json"


class Course(ICourse):
    """
    Class for writing and adding some info about course to JSON file (teachers and courses)
    """

    def __init__(self, name, teacher, course_program):
        self.__name = name
        self.__teacher = teacher
        self.__course_program = course_program

    @property
    def name(self):
        """
        name getter
        """
        return self.__name

    @name.setter
    def name(self, value):
        """
        name setter
        """
        if not isinstance(value, str):
            raise TypeError("Name has to be str type only!")
        self.__name = value

    @property
    def teacher(self):
        """
        teacher getter
        """
        return self.__teacher

    @teacher.setter
    def teacher(self, value):
        """
        teacher setter
        """
        if not isinstance(value, Teacher):
            raise TypeError("Teacher has to be Teacher type only!")
        self.__teacher = value


    @property
    def course_program(self):
        """
        course program getter
        """
        return self.__course_program


    @course_program.setter
    def course_program(self, value):
        """
        course program setter
        """
        if not isinstance(value, list):
            raise TypeError("Program has to be list type only!")
        self.__course_program = value


    def course_info(self, teachers=False):
        """
        Method for making a dictionary for future JSON writing
        """
        course = {}
        course["name"] = self.name
        course["course_program"] = self.course_program
        if not teachers:
            course["teacher"] = self.teacher.name
        if isinstance(self, LocalCourse):
            course["type"] = "Local course"
            course["laboratory"] = self.office
        elif isinstance(self, OffsiteCourse):
            course["type"] = "Offsite course"
            course["city"] = self.city
        return course


    def write_course(self):
        """
        Method for writing info about course to course.json
        """
        with open(COURSES, "r") as file:
            tmp = json.load(file)
        tmp.append(self.course_info())
        with open(COURSES, "w") as file:
            json.dump(tmp, file)


    def add_course_to_teacher(self):
        """
        Method for writing info about course to teachers.json
        """
        with open(TEACHERS, "r") as file:
            tmp = json.load(file)
        for elem in tmp:
            if elem.get(self.teacher.name):
                table = elem[self.teacher.name]
                table.append(self.course_info(True))
                break
        else:
            tmp.append({self.teacher.name: [self.course_info(True)]})
        with open(TEACHERS, "w") as file:
            json.dump(tmp, file)


    def __str__(self):
        """
        Overwriting str method
        """
        return f'Course name: {self.name}\nCourse teacher: {self.teacher.name}\n' \
               f'Course program{", ".join(self.course_program)}'


class LocalCourse(ILocalCourse, Course):
    """
    Class for creating Local course
    """

    def __init__(self, name, teacher, program, office):
        super().__init__(name, teacher, program)
        self.__office = office
        self.write_course()
        self.add_course_to_teacher()

    @property
    def office(self):
        """
        Office getter
        """
        return self.__office

    @office.setter
    def office(self, value):
        """
        Office setter
        """
        if not isinstance(value, str):
            raise TypeError("Office has to be str type only!")
        self.__office = value

    def __str__(self):
        """
        Overwriting str method
        """
        return f'Course name: {self.name}\nCourse teacher: {self.teacher.name}\n' \
               f'Course program: {", ".join(self.course_program)}\nOffice: {self.office}'


class OffsiteCourse(IOffsiteCourse, Course):
    def __init__(self, name, teacher, program, city):
        super().__init__(name, teacher, program)
        self.__city = city
        self.write_course()
        self.add_course_to_teacher()

    @property
    def city(self):
        """
        City getter
        """
        return self.__city

    @city.setter
    def city(self, value):
        """
        City setter
        """
        if not isinstance(value, str):
            raise TypeError("City has to be str type only!")
        self.__city = value

    def __str__(self):
        """
        Overwriting str method
        """
        return f'Course name: {self.name}\nCourse teacher: {self.teacher.name}\n' \
               f'Course program: {", ".join(self.course_program)}\nCity: {self.city}'


class Teacher(ITeacher):
    """
    Class that stores info about teacher
    """

    def __init__(self, name):
        self.__name = name
        self.__courses = ", ".join(self.courses())

    @property
    def name(self):
        """
        Name getter
        """
        return self.__name

    @name.setter
    def name(self, value):
        """
        Name setter
        """
        if not isinstance(value, str):
            raise TypeError("Name has to be str type only!")
        self.__name = value

    def courses(self):
        """
        Method for getting an array with courses' names
        """
        with open(TEACHERS, "r") as file:
            tmp = json.load(file)
        arr_courses = []
        arr_names = []
        if len(tmp):
            for elem in tmp:
                if elem.get(self.name):
                    arr_courses.append(elem.get(self.name))
            if len(arr_courses):
                for every in arr_courses[0]:
                    arr_names.append(every["name"])
        return arr_names

    def __str__(self):
        """
        Overwriting str method
        """
        return f'Teacher: {self.name}\nCourses: {self.__courses}'


def typer(typ, name, teacher, program, value):
    """
    Function that chose correct type of course
    """
    types = {
        "Local": LocalCourse,
        "Offsite": OffsiteCourse,
    }
    return types[typ](name, teacher, program, value)


class CourseFactory(ICourseFactory):
    """
    General class, where create courses and teachers
    """

    def create_course(self, typ, name, teacher, program, value):
        """
        Method for creating some course
        """
        if not (typ == "Local" or typ == "Offsite"):
            raise ValueError("Only Local or Offsite")
        typer(typ, name, teacher, program, value)

    def create_teacher(self, name):
        """
        Method for creating some teacher
        """
        return Teacher(name)

    def courses(self):
        """
        Method for getting info about all courses
        """
        with open(COURSES, "r") as file:
            return json.load(file)


def main():
    course_factory = CourseFactory()
    elon_musk = course_factory.create_teacher("Elon Musk")
    haudi_ho = course_factory.create_teacher("Haudi Ho")
    course_factory.create_course("Local", "PYTHON FOR 1 HOUR FROM HAUDI HO", elon_musk, ["Start", "Middle", "End"],
                                 "UnitFactoryOffice")

    course_factory.create_course("Offsite", "PYTHON FOR 1 HOUR FROM HAUDI HO", haudi_ho, ["1", "2", "4", "3"], "Kyiv")
    course_factory.create_course("Local", "PYTHON FOR 2 HOURS FROM HAUDI HO", elon_musk,
                                 ["Start", "Middle", "First End" "Second End"],
                                 "UnitFactoryOffice")


if __name__ == "__main__":
    main()
