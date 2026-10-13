class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []
        for c in s:
            if not st:
                st.append((1, c))
            elif st:
                if st[-1][1] == c:
                    if st[-1][0] == k -1:
                        for i in range(k-1):
                            st.pop()
                    else:
                        st.append((st[-1][0] + 1, c))
                else:
                    st.append((1, c))
        return ''.join([e[1] for e in st])

            

