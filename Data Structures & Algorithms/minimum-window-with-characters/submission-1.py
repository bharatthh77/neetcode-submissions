class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d1 = defaultdict(int)

        for e in t:
            d1[e] += 1
        
        d2 = defaultdict(int)
        res, res_len = [-1, -1], float('inf')
        l = 0

        have, need = 0, len(d1)
        
        for r in range(len(s)):
            c = s[r]

            d2[c] += 1

            if c in d1 and d2[c] == d1[c]:
                have += 1

            while have == need:
                if (r-l + 1) < res_len:
                    res = [l, r]
                    res_len = r-l+1

                d2[s[l]] -= 1
                if s[l] in d1 and d2[s[l]] < d1[s[l]]:
                    have -= 1
                l += 1
            
        l, r = res

        return s[l: r + 1] if res_len != float('inf') else ''

        
                
