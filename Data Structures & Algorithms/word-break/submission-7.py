class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True  # empty string base case

        for i in range(1, len(s) + 1):
            for word in wordSet:
                start = i - len(word)
                if start >= 0 and dp[start] and s[start:i] == word:
                    dp[i] = True
                    break

        return dp[len(s)]
        