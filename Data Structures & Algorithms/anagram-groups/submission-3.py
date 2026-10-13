class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        res = []
        for s in strs:
            sorted_s = str(sorted(s))
            d[sorted_s].append(s)
        
        for e in d.values():
            res.append(e)

        return res
