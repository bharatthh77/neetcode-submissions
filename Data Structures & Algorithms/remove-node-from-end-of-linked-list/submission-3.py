# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        totalLen = 0

        cur = head
        while cur:
            totalLen += 1
            cur = cur.next

        
        fromStart = totalLen - n

        if fromStart == 0:
            return head.next

        curInd = 0
        cur = head

        while curInd != fromStart - 1 and cur and cur.next:
            cur = cur.next
            curInd += 1

        temp = cur.next
        if not temp:
            return None
        else:
            cur.next = temp.next


        return head

