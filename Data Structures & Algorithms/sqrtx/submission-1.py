class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        l = 1
        r = x

        while l <= r:
            mid = (l+r)//2

            sq = mid * mid

            if sq == x:
                return mid
            elif sq > x:
                r = mid -1
            elif sq < x:
                l = mid + 1

        return r    