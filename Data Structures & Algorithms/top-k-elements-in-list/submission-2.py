class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        res = []
        for num, freq in c.most_common(k):
            res.append(num)
        return res