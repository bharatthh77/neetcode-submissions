class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            2: ['a','b','c'],
            3: ['d','e','f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
            }
        
        res = []

        def backtrack(i, li):
            nonlocal res

            if len(li) == len(digits):
                res.append(li[:])
                return
            
            dig = digits[i]

            for e in d[int(dig)]:
                li.append(e)
                backtrack(i+1, li)
                li.pop()

        if not digits:
            return [] 
        backtrack(0, [])
        res = [''.join(e) for e in res]
        return res
