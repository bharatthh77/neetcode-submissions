class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        minHeap = [-e for e in c.values()]
        print(minHeap)
        heapq.heapify(minHeap)

        q = deque()
        time = 0

        while minHeap or q:
            time += 1
            if minHeap: 
                cur = heapq.heappop(minHeap)
                print(cur)
                cur += 1
                if cur < 0:
                    q.append([cur, time + n])
            
            if q and q[0][1] <= time:
                heapq.heappush(minHeap, q.popleft()[0])
        
        return time
            
            
