class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''

        minLen = len(min(strs, key = lambda x: len(x)))

        for i in range(minLen):
            res += strs[0][i]
            for e in strs:
                if not e.startswith(res):
                    return res[:-1]
            
        return res

            