class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for p, v in zip(position, speed):
            pairs.append((p, v))
        
        pairs.sort(reverse=True)
        st =[]

        for p, v in pairs:   
            time = ((target - p )/ v)
            if not st:
                st.append(time)
            elif st and st[-1] < time:
                st.append(time)

        return len(st)