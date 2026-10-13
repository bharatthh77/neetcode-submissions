class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(-1, -1), Node(-1, -1)
        self.left.next = self.right
        self.right.prev = self.left


    def insert(self, node):
        temp = self.left.next
        self.left.next = node
        node.prev = self.left
        node.next = temp
        temp.prev = node

    def remove(self, node):
        next = node.next
        prev = node.prev
        prev.next = next
        next.prev = prev
        

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
        else: 
            if len(self.cache) == self.cap:
                lru = self.right.prev
                self.remove(lru)
                del self.cache[lru.key]
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

            
        
        
        
