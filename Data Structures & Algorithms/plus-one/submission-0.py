class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        
        carry = 0
        for i in range(len(digits)):
            s = 0

            if i == 0:
                s = digits[i] + 1
            else: 
                s = digits[i] + carry
            
            if s > 9:
                units = int(math.fmod(s, 10))
                tens = int(s/10)

                digits[i] = units
                carry = tens
            else:
                digits[i] = s
                carry = 0

        if carry != 0:
            digits.append(carry)

        digits.reverse()

        return digits

                


