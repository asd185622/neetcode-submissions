# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # ans = False
        
        # def dfs(root1):
        #     nonlocal ans
        #     if root1 and not ans:
        #         if root1.val == subRoot.val:
        #             ans = isSameTree(root1,subRoot)
        #         dfs(root1.left)
        #         dfs(root1.right)

        def dfs(root):
            if not root:
                return False

            current = isSameTree(root,subRoot)
            left = dfs(root.left)
            right = dfs(root.right)

            return current or left or right

        def isSameTree(root1,root2):
            if not root1 and not root2:
                return True
            if root1 and root2 and root1.val == root2.val:
                left = isSameTree(root1.left,root2.left)
                right = isSameTree(root1.right,root2.right)
                return left and right
            else:
                return False

        return dfs(root)
