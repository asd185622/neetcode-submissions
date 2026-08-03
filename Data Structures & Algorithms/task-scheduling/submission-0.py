class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        wordDict = {}
        for word in tasks:
            wordDict[word] = wordDict.get(word,0) + 1
        
        maxHeap = []
        for val in wordDict.values():
            maxHeap.append(-val)
        
        heapq.heapify(maxHeap)
        # print(maxHeap)

        time = 0
        q = deque()
        # print(maxHeap,q)

        while maxHeap or q:
            time += 1
            # print(maxHeap,q)

            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt:
                    q.append((cnt,time + n))
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap,q.popleft()[0])
        return time