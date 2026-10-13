class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        l = 0
        res = 0
        for r in range(len(s)):
            # print(l, r, d)
            if s[r] in d:
                if l < d[s[r]] + 1:
                    l = d[s[r]] + 1
            d[s[r]] = r

            res = max(res, r - l + 1)
            # print(l, r, res)

        return res


            