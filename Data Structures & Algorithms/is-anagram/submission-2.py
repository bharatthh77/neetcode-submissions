class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d1 = defaultdict(int)
        d2 = defaultdict(int)

        for i,j in zip(s, t):
            d1[i] += 1
            d2[j] += 1

        return d1 == d2