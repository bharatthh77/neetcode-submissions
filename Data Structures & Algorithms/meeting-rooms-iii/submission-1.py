class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        count = [0] * n
        h = [(0, i) for i in range(n)]


        for s, e in meetings:
            while h[0][0] < s:
                endTime, meetingRoom = heapq.heappop(h)
                heapq.heappush(h, (s, meetingRoom))

            eT, mR = heapq.heappop(h)
            count[mR] += 1
            heapq.heappush(h, (eT + e - s, mR))
            
        maxVal = max(count)

        return count.index(maxVal)


        