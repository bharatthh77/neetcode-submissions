class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        minHeap = []
        intervals.sort()
        res = {}

        i = 0
        for e in sorted(queries):
           
            while i < len(intervals) and e >= intervals[i][0]:
                l, r = intervals[i]
                heapq.heappush(minHeap, ((r -l +1), r))
                i += 1

            
            while minHeap and minHeap[0][1] <e:
                heapq.heappop(minHeap)

            if minHeap:
                res[e] = minHeap[0][0]
            else:
                res[e] = -1
            
        return [res[q] for q in queries]
