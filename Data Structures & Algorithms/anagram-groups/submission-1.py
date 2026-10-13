class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            sortedStr = ''.join(sorted(s))
            d[sortedStr].append(s)
        
        return [e for e in d.values()]

