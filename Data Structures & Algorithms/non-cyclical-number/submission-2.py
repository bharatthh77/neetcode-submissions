class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
    
        while n not in s:
            s.add(n)
            num = 0
            while n:
                d = int(math.fmod(n, 10))
                n = int(n/10)
                num += (d*d)
            if num == 1:
                return True
            n = num
        
        return False
        
        
