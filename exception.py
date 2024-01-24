
if __name__ == '__main__':
    num = 5

    try:
        divider = int(input())
    except ValueError:
        print("Error while parsing input value to integer.")
        # exit(1)

    try:
        print(num / divider)
    except (ZeroDivisionError, NameError) as e:
        print(f"Error: {e}")
    finally:
        print("finaaaaly")
