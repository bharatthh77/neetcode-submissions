class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        tot = len(s)
        res = ''
        for i in range(tot):
            l = i
            r = i
                    
            while l >= 0 and r < tot and s[l] == s[r]:
                curRes = s[l: r+1] 
                if len(curRes) > len(res):
                        res = curRes

                l -= 1
                r += 1

            l = i
            r = i + 1
            while l >= 0 and r < tot and s[l] == s[r]:
                curRes = s[l: r+1] 
                if len(curRes) > len(res):
                        res = curRes

                l -= 1
                r += 1

        return res
            



                








    