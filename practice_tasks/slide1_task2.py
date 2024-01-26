from collections import Counter


if __name__ == '__main__':
    full_string = "aagghnccccafvvvb"
    c = Counter(full_string)
    print(c)

    d = {
        # 'a': 2
    }
    for v in full_string:
        if v in d:
            d[v] += 1
        else:
            d[v] = 1

    print(d)