class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        int1 = int(num1)
        int2 = int(num2)

        if int1 == 0 or int2 == 0:
            return str(0)
        
        prod = int1 * int2

        return str(prod)


        