class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        hp = []
        res = []

        for e in arr:
            absVal = abs(e-x)
            heapq.heappush(hp, (absVal, e))

        while k > 0:
            res.append(heapq.heappop(hp)[1])
            k -=1

        return sorted(res)


