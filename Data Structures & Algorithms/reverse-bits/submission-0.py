class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:]
        rev_bin = binary[::-1]
        
        for _ in range(32 - len(rev_bin)):
            rev_bin += '0'

        return int(rev_bin, 2)
        


        
