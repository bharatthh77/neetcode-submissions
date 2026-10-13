class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for i in range(k+1):
            tempSrc = prices.copy()

            for s,d,c in flights:

                if prices[s] == float('inf'):
                    continue

                if prices[s] + c < tempSrc[d]:
                    tempSrc[d] = prices[s] + c

            prices = tempSrc

        return -1 if prices[dst] == float('inf') else prices[dst]