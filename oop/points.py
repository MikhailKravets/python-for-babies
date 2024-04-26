from typing import Any


class Point:

    def __init__(self, x: float, y: float) -> None:  # Constructor
        self.x = x
        self.y = y
        self.furehfuiewhfuie = "fhuewheu"

    def to_rad(self):
        return self.x**0.5

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __call__(self) -> Any:
        return self.x + self.y


class RadPoint(Point):

    def __init__(self, x: float) -> None:
        super().__init__(x, 0)

    def to_rad(self):
        raise ValueError("Cannot call to_rad from radial point")


class Triple:

    def method(self) -> str:
        return "DDD"


def to_rad(p: Point) -> [float, float]:
    pass


def get_string(s: str):
    pass


class Math:

    @staticmethod
    def custom_pow(x: int):
        return x**2


if __name__ == "__main__":
    x1, y1 = 0, 0
    x2, y2 = 0, 0
    x3, y3 = 0, 0
    x4, y4 = 0, 0

    p1 = (0, 0)
    p2 = (1, 1)
    p3 = (1, 0)
    p4 = (0, 4)

    p1 = Point(0, 1)
    print(p1)
    print(p1())

    radp1 = RadPoint(1)
    radp1.to_rad()
    RadPoint.to_rad(radp1)
    s = "string"

    print(Math.custom_pow())
