import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # nums = [-x for x in nums]
        heapq.heapify(nums)
        self.heap = nums
        self.k = k

    def add(self, val: int) -> int:
        print(self.heap)
        heapq.heappush(self.heap, val)
        print(self.heap)
        return heapq.nlargest(self.k, self.heap)[-1]
          