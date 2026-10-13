class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = []
        res = []
        nextGreater = [-1] * len(nums2) 

        for i,num in enumerate(nums2):
            while st and st[-1][0] < num:
                cur = st.pop()
                nextGreater[cur[1]] = num
            st.append((num, i))
        
        
        for e in nums1:
            ind = nums2.index(e)
            res.append(nextGreater[ind])
        
        return res

