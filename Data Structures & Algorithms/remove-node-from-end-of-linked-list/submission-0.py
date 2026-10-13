# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tot = 0

        cur = head

        while cur:
            tot += 1
            cur = cur.next
        
        from_start = tot - n

        print(from_start)

        if from_start == 0:
            return head.next

        cur = head
        i = 0
        while cur : 
            if from_start-1 == i:
                cur.next = cur.next.next
                return head
            i += 1
            cur = cur.next
        
            

        

