# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        fast, slow = head.next, head
        while slow and fast:
            print(slow.val)
            print(fast.val)
            if slow == fast:
                return True
            
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return False
        return False