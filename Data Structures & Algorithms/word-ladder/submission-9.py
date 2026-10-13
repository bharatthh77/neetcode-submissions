class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        
        if endWord not in wordSet:
            return 0

        q = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)

        while q:
            cur, d = q.popleft()

            visited.add(cur)

            if cur == endWord:
                return d 
            for i in range(len(cur)):
                for e in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = cur[:i] + e + cur[i+1:]
                    if newWord in wordSet and newWord not in visited:
                        q.append((newWord, d+1))

        return 0
            