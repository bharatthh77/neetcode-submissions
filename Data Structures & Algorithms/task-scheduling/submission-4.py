class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)

        maxHeap = [-e for e in c.values()]

        heapq.heapify(maxHeap)

        q = deque()
        time = 0

        while maxHeap or q:
            time += 1
            if maxHeap:
                cur = heapq.heappop(maxHeap)
                cur += 1
                if cur < 0:
                    q.append((cur, time + n))

            if q and q[0][1] <= time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time

                