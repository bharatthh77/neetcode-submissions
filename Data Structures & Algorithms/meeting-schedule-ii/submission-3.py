"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        
        if not intervals:
            return 0

        for e in intervals:
            print(e.start, e.end)  

        res = 1
        minHeap = [intervals[0].end]

        for e in intervals[1:]:
            prevEnd = heapq.heappop(minHeap)
            if e.start < prevEnd:
                res += 1
                heapq.heappush(minHeap, e.end)
                heapq.heappush(minHeap, prevEnd)
            else:
                heapq.heappush(minHeap, e.end)
        
        return res
