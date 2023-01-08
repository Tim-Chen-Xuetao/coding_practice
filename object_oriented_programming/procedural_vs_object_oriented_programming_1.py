
"""
Procedural Programming
"""


def show_major(student):

    if student == "John":
        print("Mechanical")
    elif student == "Tom":
        print("Electrical")
    elif student == "Lucy":
        print("Computer")
    else:
        print("Unknown student")


def demo_procedural_programming():
    a, b, c, d = "John", "Tom", "Lucy", "Mike"

    show_major(a)
    show_major(b)
    show_major(c)
    show_major(d)

"""
Object Oriented Programming
"""


class Student:
    def __init__(self, name, major):
        self._name = name
        self._major = major

    def show_major(self):
        print(self._major)


def demo_oop():
    a = Student("John", "Mechanical")
    b = Student("Tom", "Electrical")
    c = Student("Lucy", "Computer")

    a.show_major()
    b.show_major()
    c.show_major()


if __name__ == "__main__":

    demo_procedural_programming()

    demo_oop()