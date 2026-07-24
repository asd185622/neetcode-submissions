# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        queue = []

        def dfs(root,h):
            if not root:
                return 
            if len(ans) == h:
                ans.append([root.val])
            else:
                ans[h].append(root.val)
            dfs(root.left,h + 1)
            dfs(root.right,h + 1)
        dfs(root,0)
        return ans
