from datetime import date


class Student:
    classroom = '101'
    address = 'Singapore'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_age(self):
        print('%s: %s' % (self.name, self.age))

    # utility function
    @staticmethod
    def is_adult(age):
        return age > 18

    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)


def demo_class_instance_variable():
    john = Student("John", 24)
    tom = Student("Tom", 23)

    print(john.age)
    john.age = 28
    print(john.age)

    print(john.classroom)
    print(tom.classroom)

    john.classroom = '102'
    print(john.classroom)
    print(tom.classroom)
    print(Student.classroom)

    Student.classroom = '103'
    del john.classroom
    print(john.classroom)
    print(tom.classroom)
    print(Student.classroom)

    # use Student.classroom for class variable


def demo_static_class_method():
    john = Student("John", 24)
    mike = Student.from_birth_year("Mike", 2002)

    print(john.age)
    print(mike.age)

    print(Student.is_adult(22))


if __name__ == "__main__":
    demo_class_instance_variable()
    demo_static_class_method()

