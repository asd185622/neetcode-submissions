class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        visit = set()
        res = 0
        directions = [(-1,0),(0,1),(1,0),(0,-1)]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    visit.add((i,j))

        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy
                    if nx < 0 or nx >= ROWS or ny < 0 or ny >= COLS:
                        continue
                    if (nx,ny) not in visit and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
                        visit.add((nx, ny))
            res += 1
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return -1
        return res - 1 if res != 0 else 0
