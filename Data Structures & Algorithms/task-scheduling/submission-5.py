class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = Counter(tasks)
        
        q = deque()
        hp = []

        for value in d.values():
            heapq.heappush(hp, -value)

        time = 0
        while q or hp:
            time += 1
            if hp:
                cur = heapq.heappop(hp)
                cur += 1
                if cur < 0:
                    q.append((cur, time + n))
                
            if q and q[0][1] <= time:
                heapq.heappush(hp, q.popleft()[0])
            
        return time



        