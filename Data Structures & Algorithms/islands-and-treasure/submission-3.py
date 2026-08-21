class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        INF = 2147483647
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        queue = deque()
        visit = set()
        length = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i,j))
                    visit.add((i,j))

        #bfs
        while queue:
            for _ in range(len(queue)):
                x,y = queue.popleft()
                grid[x][y] = length
                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                        continue
                    if (nx,ny) not in visit and grid[nx][ny] == INF:
                        queue.append((nx,ny))
                        visit.add((nx,ny))
            length += 1
                    
        