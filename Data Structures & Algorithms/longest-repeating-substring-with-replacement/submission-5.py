class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        d = defaultdict(int)
        maxChar = 0
        res = 0

        for r in range(len(s)):
            d[s[r]] += 1

            maxChar = max(maxChar, d[s[r]])

            while (r-l + 1) - maxChar > k:
                d[s[l]] -= 1
                l += 1

            res = max(res, r-l + 1)
        return res
                
            
            

            
            

            