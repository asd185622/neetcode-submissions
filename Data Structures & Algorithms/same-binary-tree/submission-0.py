# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        ans = True
        def dfs(root1,root2):
            nonlocal ans
            if(root1 and root2):
                if root1.val != root2.val:
                    ans = False
                    return
                dfs(root1.left,root2.left)
                dfs(root1.right,root2.right)
            elif(not root1 and root2):
                ans = False
            elif(root1 and not root2):
                ans = False
        dfs(p,q)
        return ans
                
