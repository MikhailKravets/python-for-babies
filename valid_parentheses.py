P = {"(": ")", "[": "]", "{": "}"}


def is_valid(s: str) -> bool:
    stack = []

    for c in s:
        if c in P:
            stack.append(c)
            continue

        try:
            bracket = stack.pop()
        except IndexError:
            return False

        if c != P[bracket]:
            return False

    return len(stack) == 0


if __name__ == "__main__":
    print(is_valid("]{}))"))
