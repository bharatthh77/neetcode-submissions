class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d = {}
        st = ""

        for i in range(len(s)):
            d[s[i]] = t[i]
        
        value_set = set(d.values())
        if len(value_set) != len(d):
            return False

        for i in range(len(s)):
            st += d[s[i]]
        
        return st == t