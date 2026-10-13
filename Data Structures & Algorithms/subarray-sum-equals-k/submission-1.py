class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        d = defaultdict(int)
        d[0] = 1
        curSum = 0

        for num in nums:
            curSum += num
            dif = curSum - k

            res += d[dif]
            
            d[curSum] += 1

        return res