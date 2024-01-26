

# Ersatz entrypoint of programm
if __name__ == '__main__':
    full_string = input("Enter value: ")

    if len(full_string) <= 2:
        raise ValueError(f"String {full_string} must have more than 2 characters")

    # f-string
    print(f"{full_string[:2]}{full_string[-2:]}")
