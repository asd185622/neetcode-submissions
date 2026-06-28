"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        #create a new List
        copyList = Node(head.val)
        l = copyList
        curr = head.next
        mapping = {head:copyList}
        while curr:
            newNode = Node(curr.val)
            mapping[curr] = newNode
            l.next = newNode
            l = l.next
            curr = curr.next
        
        curr = head
        l = copyList
        while curr:
            if curr.random:
                l.random = mapping[curr.random]
            l = l.next
            curr = curr.next
        return copyList