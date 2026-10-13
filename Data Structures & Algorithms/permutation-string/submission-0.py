class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        l_s1 = len(s1)

        d = dict(Counter(s1))

        l = 0
        r = l_s1 - 1

        while r < len(s2):
            curr_d = dict(Counter(s2[l:r+1]))
            print(curr_d)
            if curr_d == d:
                return True
            l += 1
            r += 1
        return False

