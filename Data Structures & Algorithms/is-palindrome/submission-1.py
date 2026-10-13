class Solution:
    def isPalindrome(self, s: str) -> bool:
        sArr = []
        for e in s:
            if e.isalnum():
                sArr.append(e.lower())
        
        l = 0
        r = len(sArr) -1

        # print(sArr)

        while l <= r:
            # print(sArr[l], sArr[r])
            if sArr[l] != sArr[r]:
                return False
            l += 1
            r -= 1
        
        return True
