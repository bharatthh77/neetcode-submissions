class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-e for e in stones]

        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x = -heapq.heappop(maxHeap)
            y = -heapq.heappop(maxHeap)

            if x == y:
                continue
            elif x > y:
                heapq.heappush(maxHeap, -(x-y))
            elif y > x:
                heapq.heappush(maxHeap, -(y-x))

        return -maxHeap[0] if maxHeap else 0
