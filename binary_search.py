
def search_in_arr(arr: list[int], target: int) -> int:
    l, r = 0, len(arr) - 1

    while l <= r:
        m = (l + r) // 2

        if arr[m] == target:
            return m

        if arr[m] > target:
            r = m - 1
        else:
            l = m + 1

    return l


def binary_sqrt(n: int) -> int:
    l, r = 1, n // 2

    while l <= r:
        m = (r + l) // 2

        sq = m * m
        if sq == n:
            return m

        if sq > n:
            r = m - 1
        else:
            l = m + 1

    return r


if __name__ == "__main__":
    nums = [1, 3, 5, 6, 7, 8, 9, 10, 14, 16, 17]
    print(search_in_arr(nums, 4))

    print(binary_sqrt(10))