class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        res = []

        for s in strs:
            s_sorted = ''.join(sorted(s))
            d[s_sorted].append(s)

        for value in d.values():
            res.append(value)

        return res        
            
