
if __name__ == "__main__":
    number: str = input("Enter number: ")

    if number.isdigit():
        print("Entered string is a number")
    else:
        print("Not a number")

    res = "Is a number" if number.isdigit() else "Not a number"
    print(res)

    # print("Is a number" if number.isdigit() else "Not a number")
