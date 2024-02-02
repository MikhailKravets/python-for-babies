"""
Удалить все дубликаты элементов с неспадающего списка.

Например, [1, 1, 2, 3, 3, 3, 5, 5, 6] -> [1, 2, 3, 5, 6]
"""

# TODO: задача **
"""
Удалить все дубликаты элементов с неспадающего списка.
Каждый элемент может быть представлен максимум в двух экземплярах.

Например, 

1. [1, 1, 2, 3, 3, 3, 5, 5, 6] -> [1, 1, 2, 3, 3, 5, 5, 6]
2. [0, 0, 0, 0, 0, 0, 0, 0, 1] -> [0, 0, 1]
3. [1, 2, 3, 6, 6, 6, 6, 6, 6, 6, 6, 7] -> [1, 2, 3, 6, 6, 7]
"""


# TODO: find an error in this code
def remove_duplicates_wrong(l: list[int]) -> list[int]:
    d = {}
    for i, v in enumerate(l):
        if v in d:
            if d[v] >= 1:
                l.pop(i)
        else:
            d[v] = 1


def remove_duplicates(l: list[int]) -> list[int]:
    s = list(set(l))
    s.sort()  # sorted(s)
    return s
    


if __name__ == "__main__":
    print(remove_duplicates([1, 1, 2, 3, 3, 3, 5, 5, 6]))
