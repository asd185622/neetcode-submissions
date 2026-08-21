class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        queue = deque()
        check = []

        #cnt initial indegree
        for u, v in prerequisites:
            edges[v].append(u)
            indegree[u] += 1

        #find 0 indegree
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            check.append(node)
            for v in edges[node]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        
        return len(check) == numCourses