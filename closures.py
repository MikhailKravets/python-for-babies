"""
Write a function that takes a list of integers
as an argument and filters that list to make it
to contain only divisible by 2 number.
"""

from typing import Callable


def filter_list(l: list[int]) -> list[int]:
    # new_list = []
    # for v in l:
    #     if v % 2 == 0:
    #         new_list.append(v)
    # return new_list
    # hard-coded
    return [v for v in l if v % 2 == 0]


def filter_f(l: list[int], f: Callable[[int], bool]) -> list[int]:
    return [v for v in l if f(v)]


def condition(v: int) -> bool:
    return v % 4 == 0


# lambda functions
condition_lambda = lambda v: v % 4 == 0


# Closure
def f():
    counter = []

    def count():
        counter.append(3)
        return counter

    return count


if __name__ == "__main__":
    n = 4
    print(filter_list([3, 4, 1, 5, 4, 3, 5, 6, 7]))
    print(filter_f([3, 4, 1, 5, 4, 3, 5, 6, 7], lambda v: v % n == 0))

    counter = f()
    # [3]
    # [3, 3]
    # [3, 3, 3]
    # [3, 3, 3, 3]
    print(counter())
    print(counter())
    print(counter())
    print(counter())
