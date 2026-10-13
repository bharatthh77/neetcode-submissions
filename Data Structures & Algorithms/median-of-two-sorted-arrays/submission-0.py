class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        temp = nums1 + nums2
        temp.sort()
        print(temp)

        tot = len(temp)

        if tot % 2 != 0:
            mid = tot // 2
            return temp[mid]
        else:
            mid1 = tot // 2
            mid2 = mid1 - 1

            res = (temp[mid1] + temp[mid2]) / 2
            return res



            

            


        
        