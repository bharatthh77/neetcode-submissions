class Solution:
    def findCheapestPrice(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int
    ) -> int:

        adj = defaultdict(list)

        for u, v, cost in flights:
            adj[u].append((v, cost))

        INF = float("inf")
        dist = defaultdict(lambda: INF)

        dist[(src, 0)] = 0

        minHeap = [(0, src, 0)]  # cost, node, flights_taken

        while minHeap:
            cost, node, flights_taken = heapq.heappop(minHeap)

            if node == dst:
                return cost

            if flights_taken == k + 1:
                continue

            if cost > dist[(node, flights_taken)]:
                continue

            for nei, price in adj[node]:
                newCost = cost + price
                newFlights = flights_taken + 1

                if newCost < dist[(nei, newFlights)]:
                    dist[(nei, newFlights)] = newCost
                    heapq.heappush(
                        minHeap,
                        (newCost, nei, newFlights)
                    )

        return -1
        