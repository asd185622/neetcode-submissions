class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        points = [i for i in range(n)]

        def union(u,v):
            u = find(u)
            v = find(v)
            if u == v:
                return
            points[u] = v
        
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
        
        for u,v in edges:
            if not isSame(u,v):
                union(u,v)
        
        group = set()
        for i in range(n):
            x = find(i)
            if x not in group:
                group.add(x)
                res += 1
        return res