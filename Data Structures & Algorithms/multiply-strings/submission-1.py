class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        res = [0] * (len(num1) + len(num2))
        
        num1 = num1[::-1]
        num2 = num2[::-1]

        for n1 in range(len(num1)):
            for n2 in range(len(num2)):
                res[n1 + n2] += int(num1[n1]) * int(num2[n2])
                res[n1 + n2 + 1] += res[n1+ n2] // 10
                res[n1+ n2] = res[n1 + n2] % 10
        
        res.reverse()
        start = 0

        while res[start] == 0:
            start += 1

        res = map(str, res[start:])

        return "".join(res)


        