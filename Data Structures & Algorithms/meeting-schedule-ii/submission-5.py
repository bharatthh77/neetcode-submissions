"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x : x.start)

        h = []

        for i,interval in enumerate(intervals):
            if not h:
                heapq.heappush(h, (interval.end, interval.start))
                continue
            
            if interval.start < h[0][0]:
                heapq.heappush(h, (interval.end, interval.start))
            else:
                heapq.heappop(h)
                heapq.heappush(h, (interval.end, interval.start))


        return len(h)


            

        