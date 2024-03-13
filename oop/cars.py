class Car:

    def __init__(self, name: str):  # self == this
        self.name = name

    def display(self):
        return f"Name: {self.name}"


class Student:

    def __init__(self, student_id: str, student_name: str) -> None:
        self.id = student_id
        self.name = student_name
        self.group = None

    def __str__(self) -> str:
        return f"Student: {self.id} {self.name} {self.group}"

    def set_group(self, group: str):
        self.group = group


def func(student: Student):
    pass


if __name__ == "__main__":
    mercedes = Car("mercedes")
    bmw = Car("BMW")

    student = Student(1, "Jon Doe")

    print(mercedes.display())
    print(bmw.display())
    print(mercedes)

    print(student)
    # <__main__.Car object at 0x104573140>
    # Student: 1 Jon Doe

    student.set_group("ttt")
    print(student)
