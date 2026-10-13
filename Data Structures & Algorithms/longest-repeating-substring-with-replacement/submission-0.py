class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_char = 0
        res = 0
        d = defaultdict(int)
        l = 0
        r = 0

        for r in range(len(s)):
            d[s[r]] += 1
            max_char = max(max_char, d[s[r]])

            while (r-l+1) - max_char > k:
                d[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)

        return res
            

