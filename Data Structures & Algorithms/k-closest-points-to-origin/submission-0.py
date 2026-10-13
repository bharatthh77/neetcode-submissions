class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = heapq.nsmallest(k, points, key=lambda e: ((e[0])**2 + (e[1])**2))

        return res
        