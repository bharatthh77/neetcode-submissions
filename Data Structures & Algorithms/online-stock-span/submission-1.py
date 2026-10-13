class StockSpanner:

    def __init__(self):
        self.st = []

    def next(self, price: int) -> int:
        self.st.append(price)
        i = -1
        res = 0
        while -i <= len(self.st) and self.st[i] <= price: 
            res += 1
            i -= 1 
            
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)