import typing
# y = f(x) == x ** 2
# x - variables

# Two types of languages
# 1. Languages with explicit typing (явная типизация)
# 2. Languages with implicit typing (неявная типизация)

# Strings.
# UTF-8 is a default encoding

# Immutable / Mutable
# Immutable:
# int
# float
# str
# bool
# tuple - кортеж
# complex

# Mutable:
# list
# dict
# set
# any custom class

# Type Casting

# Collection Slice
# [n:m)

# Type Hinting
def f(s: str | int) -> str | int:
    """Docstring

    Args:
        s (str | int): _description_

    Returns:
        str | int: _description_
    """
    return s * 3

if __name__ == "__main__":
    s: str = "dog doesn't barking, in the house"
    s1 = 'I don\'t go to swimming pool'
    s2 = """one two"""
    s3 = '''ger wee'''
    # print(s.split())

    d = "25"
    # f-string
    # print(f"Variable is {d}")

    d = complex(d)
    # print(d)

    l = ["one", "two", "three", "four", "five", "six", "seven"]
    # print(len(l))

    t = (1, 2, 3)
    # print(len(t))
    # print(len(s))

    # print(l[0:5])

    # Dict (dictionary). Other languages Map
    d = {
        "one": 1,
        "two": 2,
        "three": 3,
    }
    # print(len(d))

    dummy_set = {"one", "two", "three"}
    # print(dummy_set.union({"three", "four"}))
    dummy_set.add("six")
    dummy_set.remove("one")

    t = ("one", "two", "three")
    x, y, z = t
    # print(x)
    print(f(5))
