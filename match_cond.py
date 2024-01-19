
from enum import Enum


class Color(Enum):
    black = 'black'
    red = 'red'
    blue = 'blue'
    white = 'white'
    yellow = 'yellow'
    pink = 'pink'


if __name__ == "__main__":
    d = {"name": "One", "framework": "django"}
    match d:
        case {"name": "two"}:
            print("one")
        case {"framework": anything}:
            print(anything)

    x = Color.white
    match x:
        case Color.black:
            print('black')
        case Color.red:
            print('red')
        case new_variable:
            print(new_variable)

    # walrus operator - оператор моржа
    if (n := len([1, 2, 3])) > 2:
        print(n)
