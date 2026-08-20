class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        points = [i for i in range(n)]
        group = n
        
        def find(u):
            if u == points[u]:
                return u
            points[u] = find(points[u])
            return points[u]
        
        def isSame(u,v):
            u = find(u)
            v = find(v)
            if u == v:
                return True
            return False
        
        def union(u,v):
            u = find(u)
            v = find(v)
            if u == v:
                return
            points[u] = v
        
        for u, v in edges:
            if isSame(u, v):
                return False
            else:
                n -= 1
                union(u, v)
        return True if n == 1 else False