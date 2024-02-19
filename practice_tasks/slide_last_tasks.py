from typing import Any


def is_empty(l: list[Any]) -> bool:
    return len(l) == 0


def contains_at_least_one(l1: list[int], l2: list[int]) -> bool:
    for v1, v2 in zip(l1, l2):
        if v1 == v2:
            return True
    return False


def sum_elements(l1: list[int], l2: list[int]) -> list[int]:
    # l = []
    # for v1, v2 in zip(l1, l2):
    #     l.append(v1 + v2)
    return [v1 + v2 for v1, v2 in zip(l1, l2)]


if __name__ == "__main__":
    l = [1, 4, 3, 5.7]

    l2 = [1, 6, 5, 6]
    l3 = [6, 7, 5, 4]
    l4 = [7, 13, 10, 10]
    print(is_empty([3, 4, 5]))
    print(is_empty([]))
    print(list(zip(l, l2, l3)))
    print(contains_at_least_one([5, 6, 1], [4, 4, 1]))
    print(sum_elements(l2, l3))
