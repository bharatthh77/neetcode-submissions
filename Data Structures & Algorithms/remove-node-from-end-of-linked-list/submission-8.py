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

        toRem = tot - n + 1

        if toRem == 1:
            return head.next

        cur2 = head
        curVal = 1
        while cur2 and curVal < toRem -1:
            cur2 = cur2.next
            curVal += 1

        cur2.next = cur2.next.next
        return head



        