class ListNode: 
    def __init__(self, val, nextNode=None):
        self.val = val
        self.next = nextNode


class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    
    def get(self, index: int) -> int:
        cur = self.head.next
        i = 0
        while cur:
            if i == index:
                return cur.val
            i += 1
            cur = cur.next
        return -1
        

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head.next
        self.head.next = newNode
        if not newNode.next:
            self.tail = newNode
        

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)
        self.tail.next = newNode
        self.tail = newNode 
        

    def remove(self, index: int) -> bool:
        pre_cur = self.head
        i = -1
        while pre_cur.next:
            if i + 1 == index:
                if pre_cur.next == self.tail:
                    self.tail = pre_cur
                pre_cur.next = pre_cur.next.next
                return True
            i += 1
            pre_cur = pre_cur.next
        return False

        

    def getValues(self) -> List[int]:
        res = []
        cur = self.head.next
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res
        
