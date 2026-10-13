class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST = {}
        mapTS = {}

        for i in range(len(s)):
            if ((s[i] in mapST and mapST[s[i]] != t[i]) or 
                (t[i] in mapTS and mapTS[t[i]] != s[i])):
                return False
            mapST[s[i]] = t[i]
            mapTS[t[i]] = s[i]
        return True