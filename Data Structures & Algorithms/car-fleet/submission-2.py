class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed_time = []
        for i in range(len(position)):
            time = (target - position[i])/speed[i]
            pos_speed_time.append([position[i], speed[i], time])

        pos_speed_time = sorted(pos_speed_time)
        print(pos_speed_time)

        rev_list = pos_speed_time[::-1]

        print(rev_list)
        stack = []
        res = 0


        max = 0
        for i,n in enumerate(rev_list):
            if not stack: 
                stack.append(n)
                max = n[2]
                res += 1
            if max >= n[2]:
                stack.append(n)
            else:
                while stack and n[2] > stack[-1][2]:
                    stack.pop()
                stack.append(n)
                max = n[2]  
                res +=1  
        return res