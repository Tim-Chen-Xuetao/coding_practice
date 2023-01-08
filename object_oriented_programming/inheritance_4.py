from encapsulation_3 import Student


class CommunityLeader(Student):
    def __init__(self, name, age, community_name):
        super().__init__(name, age)
        self._community = community_name

    def demonstrate_skillset(self):
        print(f"{self.name} at {self.get_age()} has organizing skill set.")


class CommunityManager(CommunityLeader):
    def __init__(self, name, age, community_name, students=None):
        super().__init__(name, age, community_name)
        if students is None:
            self._managed_students = []
        else:
            self._managed_students = students

    def add_student(self, student):
        if student not in self._managed_students:
            self._managed_students.append(student)

    def remove_student(self, student):
        if student in self._managed_students:
            self._managed_students.remove(student)

    def print_community_student(self):
        for student in self._managed_students:
            student.show_info()

    def demonstrate_skillset(self):
        print(f"{self.name} at {self.get_age()} has management skill set.")


if __name__ == "__main__":
    john = Student("John", 24)
    jack = Student("Jack", 18)

    tom = CommunityLeader("Tom", 25, "software")
    lucy = CommunityManager("Lucy", "28", "software", [tom])

    tom.demonstrate_skillset()
    lucy.demonstrate_skillset()
    print('*' * 5)

    lucy.print_community_student()
    print('*' * 5)

    lucy.add_student(john)
    lucy.add_student(jack)
    lucy.print_community_student()
    print('*' * 5)

    lucy.remove_student(tom)
    lucy.print_community_student()
