class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        print(nums)
        for i,n in enumerate(nums):
            if n > 0:
                break
            
            print(n)

            target = 0 - n

            l = 0
            r = len(nums)-1
            
            while l < r:
                if l == i:
                    l +=1
                elif r == i:
                    r -= 1
                elif nums[l] + nums[r] == target:
                    ans = [nums[l], nums[r], n]
                    ans.sort()
                    res.add(tuple(ans))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
        
        return list(res)
            
                
                            
            