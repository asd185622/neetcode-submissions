# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def dfs(root,h):
            if root:
                if len(ans) < h:
                    ans.append(root.val)
                    # print(ans,h,root.val)
                else:
                    # print(h)
                    ans[h - 1] = root.val
                dfs(root.left,h + 1)
                dfs(root.right,h + 1)
        dfs(root,1)
        return ans