"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # if not node:
        #     return None

        # clone = {}
        # queue = deque([node])

        # clone[node] = Node(node.val)

        # while queue:
        #     cur = queue.popleft()

        #     for nei in cur.neighbors:

        #         if nei not in clone:
        #             # ① 建立 nei 的 clone
        #             # ② nei 加入 queue
        #             clone[nei] = Node(nei.val)
        #             queue.append(nei)

        #         # ③ 把 nei 的 clone
        #         # 加進 cur 的 clone 的 neighbors
        #         clone[cur].neighbors.append(clone[nei])

        # # 最後到底應該 return 哪一個 Node？
        # return clone[node]
        if not node:
            return None

        clone = {}

        def dfs(copyNode):
            if copyNode in clone:
                return clone[copyNode]
            
            clone[copyNode] = Node(copyNode.val)

            for nei in copyNode.neighbors:
                nei = dfs(nei)  
                clone[copyNode].neighbors.append(nei)
            return clone[copyNode]
        dfs(node)
        return clone[node]


