class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)

            if x > y:
                x = x-y
                heapq.heappush(stones, -x)
            elif y < x:
                y = y-x 
                heapq.heappush(stones, -y)
            
        
        return -(stones[0]) if len(stones) > 0 else 0
        
