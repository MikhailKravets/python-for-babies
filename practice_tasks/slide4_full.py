import random
from typing import Any


# TODO: google what is shallow copy vs deep copy
def randomize(collection: list[int]) -> list[int]:
    new_collection = collection.copy()  # shallow copy
    random.shuffle(new_collection)
    return new_collection


def to_str_any(collection: list[Any]) -> str:
    # s = ""
    # for v in collection:
    #     s += str(v)
    return ", ".join([str(v) for v in collection])


def to_str(collection: list[str]) -> str:
    return ", ".join(collection)


def get_index(collection: list[int], value: int) -> int:
    return collection.index(value)  # -1


if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    res = randomize(l)
    print(l)
    print(res)

    print(to_str_any([1, 4, 5.5, "vvv", None]))
    print(to_str(["one", "two", "three", "four", "five", "six", "seven"]))

    print(get_index(l, 2))
