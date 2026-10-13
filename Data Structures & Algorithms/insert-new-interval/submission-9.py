class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        insertIndex = 0

        res = []

        for i in range(len(intervals)):
            if newInterval[0] > intervals[i][0]:
                insertIndex += 1
            else:
                break
            
        
        intervals.insert(insertIndex, newInterval)

        for i, interval in enumerate(intervals):
            if not res:
                res.append(interval)
                continue
            if interval[0] <= res[-1][1]:
                res[-1][0] = min(res[-1][0], interval[0])
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)

        return res