class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        cur = self.d.get(key, [])
        cur.append([value, timestamp])
        self.d[key] = cur
        

    def get(self, key: str, timestamp: int) -> str:
        cur = self.d.get(key, [])
        # print(cur)
        # print(self.d)
        res = ""

        if not cur:
            return res
        
        l = 0
        r = len(cur) -1

        while l <= r:
            mid = l + (r-l)//2

            if cur[mid][1] == timestamp:
                return cur[mid][0]

            if cur[mid][1] < timestamp:
                res = cur[mid][0]
                l = mid + 1
            elif cur[mid][1] > timestamp: 
                r = mid -1
        return res
                
