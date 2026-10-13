class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx = 0
        resLen = 0
        res = ""
        for i in range(len(s)):
            l = r = i
            # print('start: ', i, l, r)
            while l >= 0 and r < len(s) and s[l:l+1] == s[r:r+1]:
                # print('loop: ', i, l, r)
                # print('res: ', res)
                # print('s[l-1:l]: ', s[l-1:l], 's[r:r+1]: ', s[r+1:r+1+1])
                if len(s[l:r+1]) > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1

            l = i
            r = i+1
            # print('2 start: ', i, l, r)
            while l >= 0 and r < len(s) and s[l:l+1] == s[r:r+1]:
                # print('loop2: ', i, l, r)
                # print('res2: ', res)
                # print('2 s[l-1:l]: ', s[l-1:l], '2 s[r:r+1]: ', s[r+1:r+1+1])
                if len(s[l:r+1]) > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1
            
        return res


