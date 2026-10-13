# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rem = 0
        dummy_head = ListNode(-1)
        dummy_head_cur = dummy_head

        cur1 = l1
        cur2 = l2
        while cur1 or cur2:
            sum = (cur1.val if cur1 else 0) + (cur2.val if cur2 else 0) + rem
            sum_str = str(sum)
            
            if len(sum_str) > 1:
                dummy_head_cur.next = ListNode(int(sum_str[1]))
                rem = int(sum_str[0])
            else: 
                dummy_head_cur.next = ListNode(sum)
                rem = 0

            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None
            dummy_head_cur = dummy_head_cur.next


        if rem > 0:
            dummy_head_cur.next = ListNode(rem)
        
        # to print
        temp_cur = dummy_head
        while temp_cur:
            print(temp_cur.val)
            temp_cur = temp_cur.next

        return dummy_head.next






        