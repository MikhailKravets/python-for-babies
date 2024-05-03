def merge(left: list[int], right: list[int]) -> list[int]:
    res = []
    l, r = 0, 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1

    while l < len(left):
        res.append(left[l])
        l += 1

    while r < len(right):
        res.append(right[r])
        r += 1

    return res


def merge_sort(nums: list[int], l: int, r: int):
    if l == r:
        return [nums[l]]

    m = (r + l) // 2
    left = merge_sort(nums, l, m)
    right = merge_sort(nums, m + 1, r)

    return merge(left, right)


if __name__ == "__main__":
    arr = [2, 1, 5, 3, 2, 6, 8, 4]
    print(merge_sort(arr, 0, len(arr) - 1))
