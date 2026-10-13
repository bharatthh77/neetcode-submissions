class MinStack:

    def __init__(self):
        self.st = []
        self.minSt = []
        

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.minSt:
            self.minSt.append(val)
        else:
            if self.minSt[-1] >= val:
                self.minSt.append(val)
            else:
                self.minSt.append(self.minSt[-1])
        

    def pop(self) -> None:
        self.minSt.pop()
        self.st.pop()
        

    def top(self) -> int:
        return self.st[-1]
        

    def getMin(self) -> int:
        return self.minSt[-1]
        
