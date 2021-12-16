from abc import ABC, abstractmethod


class ICourse(ABC):
    """
    Interface for courses of two types (local course, offsite course)
    """

    @property
    @abstractmethod
    def name(self):
        """must be implemented"""
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        """must be implemented"""
        pass

    @property
    @abstractmethod
    def teacher(self):
        """must be implemented"""
        pass

    @teacher.setter
    @abstractmethod
    def teacher(self, value):
        """must be implemented"""
        pass

    @property
    @abstractmethod
    def course_program(self):
        """must be implemented"""
        pass

    @course_program.setter
    @abstractmethod
    def course_program(self, value):
        """must be implemented"""
        pass

    @abstractmethod
    def course_info(self):
        """must be implemented"""
        pass

    @abstractmethod
    def write_course(self):
        """must be implemented"""
        pass

    @abstractmethod
    def add_course_to_teacher(self):
        """must be implemented"""
        pass

    @abstractmethod
    def __str__(self):
        """must be implemented"""
        pass


class ILocalCourse(ABC):
    """
    Interface for class that has to implement (ICourse and ILocalCourse)
    """

    @property
    @abstractmethod
    def office(self):
        """must be implemented"""
        pass

    @office.setter
    @abstractmethod
    def office(self, value):
        """must be implemented"""
        pass


class IOffsiteCourse(ABC):
    """
    Interface for class that has to implement (ICourse and IOffsiteCourse)
    """

    @property
    @abstractmethod
    def city(self):
        """must be implemented"""
        pass

    @city.setter
    @abstractmethod
    def city(self, value):
        """must be implemented"""
        pass


class ITeacher(ABC):
    """
    Interface for Teacher class
    """

    @property
    @abstractmethod
    def name(self):
        """must be implemented"""
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        """must be implemented"""
        pass

    @abstractmethod
    def courses(self):
        """must be implemented"""
        pass

    @abstractmethod
    def __str__(self):
        """must be implemented"""
        pass


class ICourseFactory(ABC):
    """
    Interface for class that will create teachers and courses
    """

    @abstractmethod
    def create_course(self, typ, name, teacher, program, value):
        """must be implemented"""
        pass

    @abstractmethod
    def create_teacher(self, name):
        """must be implemented"""
        pass

    @abstractmethod
    def courses(self):
        """must be implemented"""
        pass
