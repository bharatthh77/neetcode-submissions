class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for n in asteroids:
            while st and st[-1] > 0 and n < 0:
                dif = st[-1] + n
                if dif < 0:
                    st.pop()
                elif dif == 0:
                    st.pop()
                    n = 0
                else:
                    n =0
            if n:
                st.append(n)
        return st

                    


            