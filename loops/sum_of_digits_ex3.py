if __name__ == "__main__":
    n = 1234
    s = 0
    # Is equal to
    # n = n // 10
    # res = n % 10

    while n > 0:
        n, res = divmod(n, 10)
        s += res
    print(s)
