class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1

        while l <= r:
            mid = l + (r-l)//2

            t = 0
            for e in piles:
                t += math.ceil(e / mid)
            
            if t > h:
                l = mid + 1
            
            elif t <= h:
                r = mid -1 

        return l
