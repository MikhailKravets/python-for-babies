
if __name__ == '__main__':
    s = input("Input numbers: ")
    i = input("Input index: ")

    try:
        i = int(i)
    except ValueError:
        print("Index value is not a number")
        exit(1)

    s = s.split()
    # y = list(map(lambda v: float(v), s))

    # y = []
    # for v in s:
    #     y.append(float(v))
    try:
        y = [float(v) for v in s]
    except ValueError:
        print("Can't cast some number from s into float.")
        exit(1)

    try:
        print(y[i])
    except IndexError:
        print(f"Index {i} doesn't exist in list y.")
