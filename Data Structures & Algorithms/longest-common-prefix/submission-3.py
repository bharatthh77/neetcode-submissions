class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''

        minLen = len(min(strs, key = lambda x: len(x)))

        for i in range(minLen):
            cur = strs[0][i]
            res += cur
            for e in strs:
                if not e[i] == cur:
                    return res[:-1]
            
        return res

            