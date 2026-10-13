class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []

        minLen = min(len(word1), len(word2))

        for i in range(minLen):
            res.append(word1[i])
            res.append(word2[i])

        strRes = ''.join(res)

        if len(word1) > minLen:
            strRes += word1[minLen:]
        elif len(word2) > minLen:
            strRes += word2[minLen:]

        return strRes            

            
            