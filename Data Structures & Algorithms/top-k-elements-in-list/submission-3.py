class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        res = []
        for e in nums:
            d[e] += 1

        sD = dict(sorted(d.items(), key = lambda x:x[1], reverse=True))

        for e in sD.items():
            while k > 0:
                res.append(e[0])
                k -= 1
                break
        
        return res
