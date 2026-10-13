# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        cur = head
        ind = 0

        l = None
        r = None

        prevL = None
        nextR = None

        while cur:
            ind += 1

            if ind == left -1:
                prevL = cur

            if ind == left:
                l = cur

            if ind == right:
                r = cur

            if ind == right + 1:
                nextR = cur

            cur = cur.next

        prev = nextR
        cur2 = l
        while cur2 != nextR:
            temp = cur2.next
            cur2.next = prev
            prev = cur2
            cur2 = temp

        if prevL:
            prevL.next = r
            return dummy.next
        else:
            return r

        
        


