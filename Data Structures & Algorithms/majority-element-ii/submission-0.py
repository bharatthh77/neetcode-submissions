class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nBy3 = n//3

        c = Counter(nums)
        res = []

        for k,v in c.items():
            if v > nBy3:
                res.append(k)
        
        return res

