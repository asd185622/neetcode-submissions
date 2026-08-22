class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adList = [[] for _ in range(numCourses)]
        queue = deque()
        res = []

        #initialize graph
        for dest, start in prerequisites:
            adList[start].append(dest)
            indegree[dest] += 1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                res.append(i)

        while queue:
            node = queue.popleft()

            for nei in adList[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
                    res.append(nei)
        return res if len(res) == numCourses else []