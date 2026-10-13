"""
Definition of Interval:
class Interval(object):, Text
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.end)
        
        # for e in intervals:
        #     print(e.start, e.end)
        if not intervals:
            return True
        
        prevEnd = intervals[0].end

        for e in intervals[1:]:
            if e.start < prevEnd:
                return False
            prevEnd = e.end
        
        return True