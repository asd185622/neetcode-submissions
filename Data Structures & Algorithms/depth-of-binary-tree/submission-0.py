# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if(not root):
            return 0
        ans = 1
        def traversal(root,h):
            nonlocal ans
            if(root):
                if(h > ans):
                    ans = h
                traversal(root.left,h + 1)
                traversal(root.right,h + 1)
        traversal(root,1)
        return ans