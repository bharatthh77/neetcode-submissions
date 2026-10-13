class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        tot = sum(weights)
        r = tot
        l = max(weights)

        while l <= r:
            # print('l: ', l, 'r: ', r)
            mid = (l+r) // 2

            curDays = 1
            curWeight = 0

            for w in weights:
                curWeight += w
                if curWeight > mid:
                    curWeight = 0
                    curDays += 1
                    curWeight += w
            # print(mid, curDays)

            if curDays <= days:
                r = mid - 1
            else:
                l = mid + 1

        return l

                
                

        