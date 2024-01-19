def f(x: str | int):
    if isinstance(x, str):
        return "reffewfew"
    elif isinstance(x, int):
        return 0
    else:
        raise ValueError("fwhufhweiu")


if __name__ == "__main__":
    x = 10
    if x > 10:
        x += 3
        print(x)
    elif x > 12:
        print(x)
    elif x > 13:
        print(x)
    else:
        print("nothing is working")

    x = "string"
    if ("s" in x and "tr" in x) or ("i" in x):
        print(x)
    else:
        print("substring is not found")

    if True:
        print("true")

    if x:  # x is not None and len(x) != 0
        print("tadaaa")
    else:
        print("something wrong")

    x = ""
    if x is not None:
        print("tadaa 2")
    else:
        print("something wrong")

    if isinstance(x, str):  # function to check variable type
        print("x is string")

    # присвоить NON-NULL к y если x is not None and len(x) != 0 иначе присвоить NULL
    y = "NON-NULL" if x else "NULL"
    print(y)
