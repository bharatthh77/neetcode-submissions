class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        t = [((e[0])**2 + (e[1])**2, e) for e in points]
        heapq.heapify(t)
        res = []

        for i in range(k):
            res.append(heapq.heappop(t)[1])

        return res
        