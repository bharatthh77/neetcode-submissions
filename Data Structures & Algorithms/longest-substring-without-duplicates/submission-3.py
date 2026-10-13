class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        l =0
        r =0
        res = 0

        if not s:
            return 0

        while r < len(s):
            if s[r] not in d:
                d[s[r]] = r
            else:
                print(d)
                res = max(res, len(d))
                old_ind = d[s[r]]
                for e in s[l:(old_ind+1)]:
                    del d[e]
                d[s[r]] = r
                l = old_ind+1
            r += 1
        return max(res, len(d))