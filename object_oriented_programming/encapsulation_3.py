from datetime import date


class Student:
    classroom = '101'
    address = 'Singapore'

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self._name_age = name + str(age)

    def show_age(self):
        print('%s: %s' % (self.__name, self.__age))

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if isinstance(age, int):
            self.__age = age
        else:
            raise ValueError

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @name.deleter
    def name(self):
        print("You tried to remove object name")

    @staticmethod
    def is_adult(age):
        return age > 18

    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)

    def show_info(self):
        print(f"name: {self.__name}; age: {self.__age}")

    def demonstrate_skillset(self):
        raise NotImplementedError


class GradePredictor:

    def predict_next_grade(self, student: Student, grade: list):
        if student.get_age() > 18:
            self._predict_adult_grade(grade)
        else:
            self._predict_non_adult_grade(grade)

    def _predict_adult_grade(self, grade):
        pass

    def _predict_non_adult_grade(self, grade):
        pass


def demo_private():
    john = Student("John", 24)
    print(john._name_age)
    # print(john.__name)


def demo_set_private():
    obj = Student("Jack", 18)
    obj.__age = 28
    print("obj.__age:  ", obj.__age)
    print("obj.get_age():  ", obj.get_age())

    obj.show_info()


def demo_property():
    obj = Student("John", 24)
    print(obj.name)

    obj.name = "Jake"
    print(obj.name)

    del obj.name

    obj.show_info()


if __name__ == "__main__":
    demo_private()
    demo_set_private()
    demo_property()