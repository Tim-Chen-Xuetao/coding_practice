

def demo_polymorphic_function():
    print(len("students"))
    print(len([10, 20, 30]))


class India:
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")


class USA:
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")


def func(obj):
    obj.capital()
    obj.language()
    obj.type()


def demo_polymorphism_class_method():
    obj_ind = India()
    obj_usa = USA()

    func(obj_ind)
    func(obj_usa)


class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")


class Sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")


class Ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")


def demo_polymorphism_inheritance_override():
    obj_bird = Bird()
    obj_spr = Sparrow()
    obj_ost = Ostrich()

    obj_bird.intro()
    obj_bird.flight()

    obj_spr.intro()
    obj_spr.flight()

    obj_ost.intro()
    obj_ost.flight()


if __name__ == "__main__":
    demo_polymorphic_function()
    print('*' * 5)

    demo_polymorphism_class_method()
    print('*' * 5)

    demo_polymorphism_inheritance_override()
