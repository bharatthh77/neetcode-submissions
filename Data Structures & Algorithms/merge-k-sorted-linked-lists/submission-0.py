# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i, l in enumerate(lists):
            heapq.heappush(heap, (l.val, i, l))
        
        dummy =  ListNode()
        cur = dummy

        while heap:
            v, i, node = heapq.heappop(heap)
            cur.next = node
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
            cur = cur.next
            cur.next = None
        
        return dummy.next

        
