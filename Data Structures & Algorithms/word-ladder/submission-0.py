class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        d = defaultdict(list)

        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                pat = word[:i] + "*" + word[i+1:]   
                d[pat].append(word)
    
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1

        while q:
            for i in range(len(q)):
                cur = q.popleft()

                if cur == endWord:
                    return res

                for j in range(len(cur)):
                    pat = cur[:j] + "*" + cur[j+1:]
                    for e in d[pat]:
                        if e not in visit:
                            q.append(e)
                            visit.add(e)
                    
            res+=1
        return 0