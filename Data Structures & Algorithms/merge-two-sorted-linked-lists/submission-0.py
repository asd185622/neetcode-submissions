# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val >= list2.val:
            curr = list2
            p1 = list1
            p2 = list2.next
        else:
            curr = list1
            p1 = list1.next
            p2 = list2
        
        ans = curr
        
        while p1 is not None and p2 is not None:
            if p1.val <= p2.val:
                curr.next = p1
                p1 = p1.next
                curr = curr.next
            else:
                curr.next = p2
                p2 = p2.next
                curr = curr.next
        
        if not p1:
            curr.next = p2
        else:
            curr.next = p1
        return ans
                