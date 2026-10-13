class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.k = k
        self.heap = nums

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        return heapq.nlargest(self.k, self.heap)[-1]
