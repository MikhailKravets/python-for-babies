
if __name__ == '__main__':
    name = "John Doe"
    print(name[::-1])

    name = name.lower()
    first, last = name.split()
    # s1, s2 = [1, 3]

    first = first[::-1].capitalize()
    last = last[::-1].capitalize()
    print(f"{first} {last}")
