import time
from typing import Callable


def timer(context: str):
    def real_dec(f: Callable[..., int]):
        def wrapper(*args, **kwargs):
            prev = time.time()
            res = f(*args, **kwargs)
            print(f"Spent time {context}: {time.time() - prev}")
            return res

        return wrapper
    return real_dec


def mock_function(x: int):
    time.sleep(3)
    return x**2


@timer("sugar")
def lock_function(x: int, y: int):
    time.sleep(1.5)
    return x ** (1 / y)


timed_function = timer("native")(mock_function)

if __name__ == "__main__":
    print(timed_function(5))
    print(lock_function(3, 4))
