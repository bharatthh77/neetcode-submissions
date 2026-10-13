class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for p, v in zip(position, speed):
            pairs.append((p, v))
        
        pairs.sort(reverse=True)
        st =[]

        for p, v in pairs:
            st.append((target - p )/ v)
            if len(st) >= 2 and st[-1] <= st[-2]:
                st.pop()
        return len(st)