# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 1

        def dfs(root,nodeList):
            nonlocal ans
            if root:
                # print(root.val,nodeList)
                if not nodeList:
                    nodeList.append(root.val)
                    dfs(root.left,nodeList)
                    dfs(root.right,nodeList)
                    return

                if root.val >= nodeList[-1]:
                    # print("append",root.val)
                    nodeList.append(root.val)
                    ans += 1
                    dfs(root.left,nodeList)
                    dfs(root.right,nodeList)
                    nodeList.pop()
                else:
                    dfs(root.left,nodeList)
                    dfs(root.right,nodeList)
        dfs(root,[])
        return ans