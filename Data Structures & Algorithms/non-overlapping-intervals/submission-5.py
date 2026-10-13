class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])

        prevEnd = intervals[0][1]
        res = 0

        for interval in intervals[1:]:
            if prevEnd > interval[0]:
                res += 1
                prevEnd = min(interval[1], prevEnd)
            else:
                prevEnd = interval[1]
        
        return res

        