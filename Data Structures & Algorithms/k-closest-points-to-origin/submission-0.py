class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        priorityQueue = []

        for point in points:
            x = point[0]
            y = point[1]
            distance = math.sqrt((x - 0) ** 2 + (y - 0) ** 2)
            heapq.heappush(priorityQueue,(distance,(x,y)))
        
        ans = []
        while k != 0:
            tmp = heapq.heappop(priorityQueue)[1]
            ans.append(tmp)
            k -= 1
        
        return ans