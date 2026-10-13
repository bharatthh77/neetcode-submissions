class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sol = []

        def backtrack(index):
            
            if index >= len(s):
                res.append(sol.copy())

            # print('index: ', index, 'sol: ', sol, 'res: ', res)

            for i in range(index, len(s)):
                temp_word = s[index:i + 1]
                
                # print(index, temp_word)
                
                if self.isPalindrom(temp_word):
                    sol.append(temp_word)
                    backtrack(i+1)
                    sol.pop()
                 

        backtrack(0)
        return res

    def isPalindrom(self, word):
        return word == word[::-1]
        