class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, n in enumerate(nums):
            if i -1 >= 0 and n == nums[i - 1]:
                continue
                
            if n > 0:
                break

            print(i,n)

            l = i + 1
            r = len(nums) -1

            while l < r:
                # print('l:', nums[l], 'r:', nums[r])

                if l > i + 1 and nums[l] == nums[l-1]:
                    l += 1
                    continue

                if r < len(nums) -2 and nums[r] == nums[r + 1]:
                    r -= 1
                    continue
                
                tot = n + nums[l] + nums[r]
                if tot == 0:
                    res.append([nums[i], nums[l] , nums[r]])
                    l += 1
                    r -= 1
                    continue

                elif tot < 0:
                    l += 1
                
                else:
                    r -= 1
        return res
            
            


            

            
            
