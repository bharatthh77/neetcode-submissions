class MinStack:

    def __init__(self):
        self.st = []
        self.minSt = []
        

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.minSt:
            self.minSt.append(val)
        elif val <= self.minSt[-1]:
            self.minSt.append(val)
        else:
            top = self.minSt[-1]
            self.minSt.append(top)
        

    def pop(self) -> None:
        self.st.pop()
        self.minSt.pop()
        

    def top(self) -> int:
        return self.st[-1]
        

    def getMin(self) -> int:
        return self.minSt[-1]
        
