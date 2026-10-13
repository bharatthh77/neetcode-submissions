class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = defaultdict(int)

        for e in nums:
            d[e] += 1
        
        print(d)

        for k,v in d.items():
            if v > 1:
                return k