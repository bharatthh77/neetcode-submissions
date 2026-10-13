class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        visits = defaultdict(list)
        for t, u, w in sorted(zip(timestamp, username, website)):  # sort by time
            visits[u].append(w)

        count = defaultdict(int)
        for webs in visits.values():
            for pat in set(combinations(webs, 3)):   # dedupe per user
                count[pat] += 1

        return list(min(count, key=lambda p: (-count[p], p)))  # most freq, then lexicographically smallest



            
        


