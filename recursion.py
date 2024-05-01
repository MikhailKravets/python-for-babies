def f(x: int):
    if x == 0:
        return 0

    y = f(x - 1)
    return x + y


def f_iter(x: int):
    c = 0
    for i in range(1, x + 1):
        c += i

    return c


def fibonacci(n: int) -> int:
    if n <= 1:
        return n

    left = fibonacci(n - 1)
    left_left = fibonacci(n - 2)

    return left + left_left


class Tree:

    def __init__(self, val: int) -> None:
        self.val = val
        self.left: None | Tree = None
        self.right: None | Tree = None


def dfs(root: Tree):
    if not root:
        return None

    dfs(root.left)
    dfs(root.right)

    return None        


if __name__ == "__main__":
    print(f(5))
    print(f_iter(5))
    print(fibonacci(5))
