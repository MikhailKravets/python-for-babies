# Single Responsibility Principle
def is_divisible(num: int) -> bool:
    return num % 3 == 0


def f(x: int) -> int:
    return x**2


if __name__ == "__main__":
    f()
