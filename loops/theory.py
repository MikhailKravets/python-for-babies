def gen(n=10):
    for i in range(n):
        yield i**0.5


if __name__ == "__main__":
    # While Loop
    i = 0
    while i < 10:
        if i == 2:
            i += 1
            continue
        print(f"Iter: {i}")
        i += 1
    print("further\n")

    # For loop
    l = [3, 4, 5, 4, 6, 4, 7, 2]
    for v in l:
        print(f"Elem: {v}")

    print("\n")

    # c++ loop example
    # for(int i = 0; i < N; i++):
    #     print(f"Elem: {v[i]}")

    # Usage of range function
    # range returns generator
    for i in range(10):
        print(f"I: {i}")

    print("\n")

    for i in range(10, 20):
        print(i)

    print("\n")

    for i in range(1, 20, 2):
        print(i)

    print(list(range(10)))

    # Use range for collection iteration
    for i in range(len(l)):
        print(l[i])

    # For loop in a nutshell
    print("\nIterators")
    it = iter([4, 5])
    print(next(it))
    print(next(it))

    try:
        print(next(it))
    except StopIteration:
        print("Stop iteration")

    # Generators
    print(f"\nGenerators")
    generator = gen(10)
    for v in generator:
        print(v)

    # List comprehension
    x = [v for v in range(-10_000, 10_000) if v != 0]
    y = [v**2 for v in x]

    # Is equal to
    xe = []
    for v in range(-10_000, 10_000):
        if v != 0:
            xe.append(v)

    ye = []
    for v in xe:
        ye.append(v)

    print("\nDict comprehension")
    # Dict Comprehension
    d = {v: v**2 for v in range(10)}
    print(d)

    # Is equal to
    de = {}
    for v in range(10):
        de[v] = v**2
    print(de)

    print("\nGen comprehension")
    new_gen = (v**2 for v in range(10))
    print(next(new_gen))
    print(next(new_gen))
    print(next(new_gen))
