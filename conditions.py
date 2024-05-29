def f(x: str | int):
    if isinstance(x, str):
        return "reffewfew"

    if isinstance(x, int):
        return 0

    raise ValueError("fwhufhweiu")


if __name__ == "__main__":
    print(141 % 7)
