class Solution:
    def simplifyPath(self, path: str) -> str:
        st = ['/']
        tot = len(path)
        print(tot)

        for i, p in enumerate(path):
            if p == '/' and st[-1] == '/':
                continue
            elif (p == '/' and st[-1] == '.'):
                if st[-2] == '.' and st[-3] == '/':
                    for i in range(2):
                        st.pop()
                    if len(st) != 1:
                        st.pop()
                    while st and st[-1] != '/':
                        st.pop()
                    continue
                elif st[-2] == '/':
                    st.pop()
                    continue
            elif i == (tot - 1) and  p == '.':
                if st[-1] == '.' and st[-2] == '/':
                    st.pop()
                    if len(st) != 1:
                        st.pop()
                    while st and st[-1] != '/':
                            st.pop()
                    continue
                elif st[-1] == '/':
                    continue

            st.append(p)
        
        if len(st) != 1:
            while st[-1] == '/':
                st.pop()
            
        return ''.join(st) 
            

