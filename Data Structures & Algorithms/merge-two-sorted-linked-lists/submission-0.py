# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        res = None
        head = None

        while curr1 or curr2:
            if curr1 is None:
                if res is None:
                    res = curr2
                    head = res
                else:
                    res.next = curr2
                return head

            if curr2 is None:
                if res is None:
                    res = curr1
                    head = res
                else:
                    res.next = curr1
                return head
                
            if curr1.val < curr2.val:
                if res is None:
                    res = curr1
                    head = res
                else:
                    res.next = curr1
                    res = curr1
                curr1 = curr1.next
            elif curr1.val >= curr2.val:
                if res is None:
                    res = curr2
                    head = res
                else:
                    res.next = curr2
                    res = curr2
                curr2 = curr2.next

        return head


