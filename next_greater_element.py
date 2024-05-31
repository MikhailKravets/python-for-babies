
def nge(nums1: list[int], nums2: list[int]) -> list[int]:
    d = {v: -1 for v in nums1}  # OrderedDict
    stack = []

    for v in nums2[::-1]:
        while stack and stack[-1] < v:
            stack.pop()

        if v in d and stack:
            d[v] = stack[-1]

        stack.append(v)

    return d.values()

if __name__ == "__main__":
    print(nge([2, 4, 3], [3, 1, 2, 4]))