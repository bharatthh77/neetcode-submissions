class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

        

    def get(self, key: str, timestamp: int) -> str:
        cur = self.d[key]

        if not cur:
            return ""
        
        l = 0
        r = len(cur)
        res = ""

        while l < r:
            mid = l + (r-l)//2
            
            if timestamp >= cur[mid][0]:
                l = mid + 1
            else: 
                r = mid

        return cur[r-1][1] if r else ""


        
