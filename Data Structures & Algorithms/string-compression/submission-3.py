class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0
        r = 0
        n = len(chars)

        while r < n:
            cur = chars[r]
            curCount = 0

            # Find the size of this group
            while r < n and chars[r] == cur:
                curCount += 1
                r += 1

            # Write the character
            chars[l] = cur
            l += 1

            # Write the count if > 1
            if curCount > 1:
                for c in str(curCount):
                    chars[l] = c
                    l += 1

        return l