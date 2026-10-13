class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        
        while n not in s:
            s.add(n)
            num = 0
            while n:
                # print('n before: ', n)
                d = int(math.fmod(n, 10))
                n = int(n/10)
                # print('n: ', n, 'd: ', d)
                num += (d*d)
            # print(num)
            if num == 1:
                return True
            n = num
        
        return False
        
        
