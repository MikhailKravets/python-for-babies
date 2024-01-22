
if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # 1 Approach
    # l.reverse()

    # 2. Approach
    print(list(reversed(l)))

    # 3. Approach
    for v in reversed(l):
        print(v)

    # 4. Approach
    # Slices
    print(l[::-1])
