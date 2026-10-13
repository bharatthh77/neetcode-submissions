class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indexes = []
        for n in nums1:
            indexes.append(nums2.index(n))
        
        res = []
        st = []
        for e in indexes:
            for i in range(e, len(nums2)):
                if not st or nums2[e] >= nums2[i]:
                    st.append(nums2[i])
                    # print('first')
                    if i == len(nums2) - 1:
                        res.append(-1)
                        st = []
                else:
                    res.append(nums2[i])
                    st = []
                    # print('second')
                    break
                # print('after', e, i, st)

        return res                                
