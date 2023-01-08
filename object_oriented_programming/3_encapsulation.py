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

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if isinstance(age, int):
            self.__age = age
        else:
            raise ValueError

    @staticmethod
    def is_adult(age):
        return age > 18

    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)


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
    obj.__name = "tom"
    print("obj.__name:  ", obj.__name)
    print("obj.get_name():  ", obj.get_name())


if __name__ == "__main__":
    demo_private()
    demo_set_private()