# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = res = ListNode()

        while l1 or l2:
            op1 = l1.val if l1 else 0
            op2 = l2.val if l2 else 0
            sum = op1 + op2 + cur.val

            print('sum: ', sum)

            carry = 0
            curVal = sum

            if sum > 9:
                carry = sum // 10
                curVal = sum % 10

            print('l1: ', op1, 'l2: ', op2, 'carry: ', carry, 'curVal: ', curVal)

            cur.val = curVal
            if (l1 and l1.next) or (l2 and l2.next) or carry > 0:
                cur.next = ListNode(carry)
                cur = cur.next

            if l1: 
                l1 = l1.next
            if l2: 
                l2 = l2.next

        return res



            
            