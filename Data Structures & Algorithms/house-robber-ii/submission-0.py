class Solution:
    def rob(self, nums: List[int]) -> int:
        total_cost = [(0, True)] * len(nums)

        if len(nums) < 3: 
            return max(nums)

        total_cost[0] = (nums[0], True)
        total_cost[1] = (nums[1], False)

        if len(nums) == 3:
            total_cost[2] = (nums[2], False)
            return max(total_cost, key=lambda x: x[0])[0]
        else:
            total_cost[2] = (nums[2] + total_cost[0][0], True)


        for i in range(3, len(nums)):
            actual2 = total_cost[i-2][0]
            actual3 = total_cost[i-3][0]
            if i == len(nums) - 1:
                if total_cost[i-2][1]:
                    actual2 -= nums[0]
                if total_cost[i-3][1]:
                    actual3 -= nums[0]

            if actual2 > actual3:
                total_cost[i] = (nums[i] + actual2, total_cost[i-2][1])
            elif actual2 < actual3:
                total_cost[i] = (nums[i] + actual3, total_cost[i-3][1])
            elif actual2 == actual3:
                if total_cost[i-2][1] and not total_cost[i-3][1]:
                    total_cost[i] = (nums[i] + actual3, total_cost[i-3][1])
                elif total_cost[i-3][1] and not total_cost[i-2][1]:
                    total_cost[i] = (nums[i] + actual2, total_cost[i-2][1])
                else:
                    total_cost[i] = (nums[i] + actual3, total_cost[i-3][1])
        
        # print(total_cost)

        return max(total_cost, key=lambda x: x[0])[0]
                
