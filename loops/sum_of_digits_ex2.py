
if __name__ == "__main__":
    n = 1234
    s = 0
    ns = str(n)
    ns = [int(v) for v in ns]
    print(sum(ns))

    # Other approach
    print(sum(map(int, str(n))))
