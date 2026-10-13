class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1.0

        temp = n
        n = abs(n)
        while n:
            res *= x
            n -= 1
        
        if temp < 0:
            res = 1/res

        return res
        