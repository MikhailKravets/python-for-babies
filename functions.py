# 1. Name of function in snake_case
# 2. Give function name based on the functionality of the function


def f(x: float) -> float:
    return x**2


# 1. Positional arguments
# Call this function as void(2, y=4)
def void(x, y):
    print(x, y)


# 2. Default value
# Call this as x, y = default(4)
def default(x: float, y: int = 5):
    return x, y


# 3. MUTABLE can't be default
# Code
# l = [3, 4]
# res = mut_default()
# res = mut_default()  # [5]
# mut_default(l)
# print(l)
# print(res)
def mut_default(l: list[int] = []):
    if not l:
        l.append(5)
    else:
        l.append(6)
    return l


def correct_mut_default(l: list[int] | None = None):
    if not l:
        l = []

    l.append(6)
    return l


# 4. args as a list
def list_arguments(*args):
    return sum(args)


# 5. args as a dict
def dict_arguments(**kwargs):
    print(kwargs)


def any_args(*args, **kwargs):
    print(args, kwargs)


# 6. some insanity
def power(a: int, b: int, *, c: int):
    pass


def max_number(numbers: list[int]) -> int:
    try:
        current_max = numbers[0]
    except ValueError:
        raise ValueError("List cannot be empty. It must contain at least one number.")

    for v in numbers[1:]:
        if v > current_max:
            current_max = v

    return current_max


if __name__ == "__main__":
    print(list_arguments(4, 5, 6, 7, 4, 3, 2))
    print(dict_arguments(one=4, random_arg_name=5, four=6))
    any_args()
    any_args(5, 6, 7, one=5, two=5)

    power(3, 4, c=5)
    print(max_number([5, 4, 3, 1, 8, 1, 2]))
