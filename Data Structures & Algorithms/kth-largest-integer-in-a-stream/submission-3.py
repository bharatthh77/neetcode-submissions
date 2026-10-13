class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.k = k
        self.hp = nums

    def add(self, val: int) -> int:
        heapq.heappush(self.hp, val)       
        return heapq.nlargest(self.k, self.hp)[-1]
