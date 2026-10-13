class MedianFinder:

    def __init__(self):
        self.minh = []
        self.maxh = []
        

    def addNum(self, num: int) -> None:
        if self.minh and num > self.minh[0]:
            heapq.heappush(self.minh, num)
        else:
            heapq.heappush(self.maxh, -num)
        
        if len(self.minh) - len(self.maxh) > 1:
            cur = heapq.heappop(self.minh)
            heapq.heappush(self.maxh, -cur)
        elif len(self.maxh) - len(self.minh) > 1:
            cur = heapq.heappop(self.maxh)
            heapq.heappush(self.minh, -cur)


    def findMedian(self) -> float:
        if len(self.minh) > len(self.maxh):
            return self.minh[0]
        elif len(self.maxh) > len(self.minh):
            return -self.maxh[0]
        else:
            return (self.minh[0] + -self.maxh[0]) / 2

        