class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtrack(i, dots, curIp):
            if dots == 4 and i == len(s):
                res.append(curIp[:-1])
            if dots > 4:
                return
            
            for j in range(i, min(i+3, len(s))):
                if i != j and s[i] == '0':
                    continue
                elif int(s[i: j+1]) < 256:
                    backtrack(j + 1, dots + 1, curIp + s[i : j + 1] + '.')
            
        backtrack(0, 0, '')

        return res