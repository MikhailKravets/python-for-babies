def display_paired(l: list[int]) -> None:
    for v in l:
        if v == 237:
            return
        if v % 2 == 0:
            print(v, end=" ")


if __name__ == "__main__":
    display_paired([2, 3, 4, 2, 5, 6, 237, 8, 8])
