class Solution:

    def __init__(self, w: List[int]):
        self.pre = [0]
        for e in w:
            self.pre.append(self.pre[-1] + e)
        print(self.pre)

    def pickIndex(self) -> int:
        target = random.random() * self.pre[-1]
        l, r = 0, len(self.pre) - 1
        while l < r:
            mid = (l+r) // 2
            if target < self.pre[mid]:
                r = mid
            elif target > self.pre[mid]:
                l = mid + 1
            else: 
                return mid -1
        return l - 1      


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()