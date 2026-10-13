class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l, r = 0, 0
        n = 0

        while r - l + 1 <= len(needle) and r < len(haystack):
            ch = needle[n]
            print('ch: ', ch)
            print('l: ', l, "r: ", r)
            if haystack[r] == ch:
                r += 1
                n += 1
            else: 
                l += 1
                r = l
                n = 0 
        if haystack[l:r] == needle:
            return l
        else: 
            return -1 

                
                

        