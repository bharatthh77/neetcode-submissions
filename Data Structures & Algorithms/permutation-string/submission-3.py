class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        l_s1 = len(s1)
        d = dict(Counter(s1))
        l = 0
        r = l_s1 - 1

        window = dict(Counter(s2[l:r+1]))

        if window == d:
            return True

        l+=1
        r+=1

        while r < len(s2):
            window[s2[r]] = window.get(s2[r], 0) + 1
            window[s2[l-1]] = window.get(s2[l-1], 0) - 1
            if window[s2[l-1]] == 0:
                del window[s2[l-1]]
            if window == d:
                return True
            l += 1
            r += 1

        return False

