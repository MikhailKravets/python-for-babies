from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word = Counter(s)
        target = Counter(t)

        if len(word) != len(target):
            return False

        for k, v in target.items():
            if k not in word or v != word[k]:
                return False
        return True


if __name__ == "__main__":
    print(Solution().isAnagram("anagram", "nagaram"))
