
from typing import Callable, Iterable


def filter_and_index(collection: list[int]) -> (list[int], list[int]):
    updated, indeces = [], []

    for i, v in enumerate(collection):
        if v % 2 != 0:
            updated.append(v)
            indeces.append(i)

    return updated, indeces


def reduce(f: Callable[[int, int], int], iterable: list[int]):
    accumulated = iterable[0]

    for v in iterable[1:]:
        accumulated = f(accumulated, v)

    return accumulated


def _f(cummulated_value: int, v: int):
    return cummulated_value + v


if __name__ == '__main__':
    l = [1, 4, 3, 5, 6, 3, 1, 2, 3, 4]
    new, ind = filter_and_index(l)
    print(new)
    print(ind)

    print(reduce(lambda c, v: c + v, l))
    print(reduce(lambda c, v: c * v, l))
    print(reduce(lambda c, v: c - v, l))

