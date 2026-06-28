# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        flag = 0
        add = 0
        dummy = ListNode(0)
        l3 = dummy
        while l1 and l2:
            add = l1.val + l2.val + flag
            flag = add // 10
            l3.next = ListNode(add % 10)
            l3 = l3.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            l1.val += flag
            flag = l1.val // 10
            l1.val %= 10
            l3.next = ListNode(l1.val)
            l1 = l1.next
            l3 = l3.next
        while l2:
            l2.val += flag
            flag = l2.val // 10
            l2.val %= 10
            l3.next = ListNode(l2.val)
            l2 = l2.next
            l3 = l3.next
        if flag:
            l3.next = ListNode(flag)
        return dummy.next