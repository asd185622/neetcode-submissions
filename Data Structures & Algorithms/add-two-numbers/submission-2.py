# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # flag = 0
        # add = 0
        # dummy = ListNode(0)
        # l3 = dummy
        # while l1 and l2:
        #     add = l1.val + l2.val + flag
        #     flag = add // 10
        #     l3.next = ListNode(add % 10)
        #     l3 = l3.next
        #     l1 = l1.next
        #     l2 = l2.next
        
        # while l1:
        #     l1.val += flag
        #     flag = l1.val // 10
        #     l1.val %= 10
        #     l3.next = ListNode(l1.val)
        #     l1 = l1.next
        #     l3 = l3.next
        # while l2:
        #     l2.val += flag
        #     flag = l2.val // 10
        #     l2.val %= 10
        #     l3.next = ListNode(l2.val)
        #     l2 = l2.next
        #     l3 = l3.next
        # if flag:
        #     l3.next = ListNode(flag)
        # return dummy.next
        dummy = ListNode(0)
        l3 = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10

            l3.next = ListNode(total % 10)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            l3 = l3.next
        return dummy.next