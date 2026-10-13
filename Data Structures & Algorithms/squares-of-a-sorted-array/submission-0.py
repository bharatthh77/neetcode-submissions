class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        for e in nums:
            res.append(e * e)
        
        res.sort()
        return res