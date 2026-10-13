class CountSquares:
    def __init__(self):
        self.pts = []
        self.ptcount = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.pts.append(point)
        self.ptcount[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        ptx, pty = point

        res = 0
        
        for x,y in self.pts:
            if (abs(ptx - x) != abs(pty-y)) or x == ptx or y == pty:
                continue
            
            res += self.ptcount[(x, pty)] * self.ptcount[(ptx, y)]
        
        return res
