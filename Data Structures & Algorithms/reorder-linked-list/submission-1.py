# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        second = None

        while slow:
            temp = slow.next
            slow.next = prev

            prev = slow
            slow = temp

        first, second = head, prev

        while second and first:
            temp1 = first.next
            temp2 = second.next
            
            first.next = second
            second.next = temp1

            first = temp1
            second = temp2


    
        


