class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        removed = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prev_end:
                removed += 1

                # Keep whichever interval ends earlier
                prev_end = min(prev_end, end)
            else:
                prev_end = end

        return removed