class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        h = []
        res = {}

        i = 0
        for e in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= e:
                l, r = intervals[i]
                heapq.heappush(h, (r - l + 1, r))
                i+=1

            while h and h[0][1] < e:
                heapq.heappop(h)

            if h:
                res[e] = h[0][0]
            else:
                res[e] = -1

        return [res[q] for q in queries]



            
