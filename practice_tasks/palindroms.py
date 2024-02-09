import re

pattern = re.compile("[\W_]+")


# AmanaplanacanalPanama
def is_palindrom(s: str) -> bool:
    s = pattern.sub("", s).lower()

    # i = 0
    # while i < len(s) // 2:
    #     i += 1
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True


if __name__ == "__main__":
    print(is_palindrom("A man, a plan, a canal Panama"))
    print(is_palindrom("race a car"))
