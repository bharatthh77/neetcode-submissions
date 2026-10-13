class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        
        sorted_list = sorted(d.items(), key = lambda x: x[1], reverse=True)

        return [e[0] for e in sorted_list[:k]]
