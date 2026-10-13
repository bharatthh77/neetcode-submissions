class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numsInd = {num: i for i, num in enumerate(nums1)}                             
        res = [-1] * len(nums1)
        st = []
        for e in nums2:
            while st and st[-1] < e:
                top = st.pop()
                res[numsInd[top]] = e
            if e in numsInd:
                st.append(e)
        return res