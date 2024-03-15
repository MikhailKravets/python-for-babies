class Car:

    def __init__(self, name: str):  # self == this
        self.name = name

    def display(self):
        return f"Name: {self.name}"

    def power(self) -> int:
        raise NotImplementedError("Method should be implemented by a child class")

    def __len__(self):
        return 10


class Mercedes(Car):

    def __init__(self, hourse_power: int):  # override
        self.hourse_power = hourse_power
        super().__init__("Mercedes")

    def power(self) -> int:
        return self.hourse_power


class BMW(Car):

    def __init__(self, hourse_power: int):  # override
        self.hourse_power = hourse_power
        super().__init__("BMW")

    def power(self) -> int:
        return self.hourse_power * 0.98


class X5(BMW):
    pass


def sum_power(*cars: tuple[Car]) -> int:
    return sum(v.power() for v in cars)


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
    mercedes = Mercedes(600)
    bmw = BMW(600)

    student = Student(1, "Jon Doe")

    print(mercedes.display())
    print(bmw.display())
    print(mercedes)

    print(sum_power(mercedes, bmw, BMW(300)))

    print(len(mercedes))

    print(student)
    # <__main__.Car object at 0x104573140>
    # Student: 1 Jon Doe

    student.set_group("ttt")
    print(student)
