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

        h = []

        for interval in intervals:
            if not h:
                heapq.heappush(h, interval.end)
            elif h[0] > interval.start:
                heapq.heappush(h, interval.end)
            else:
                heapq.heappop(h)
                heapq.heappush(h, interval.end)
            
        return len(h)

                        


            