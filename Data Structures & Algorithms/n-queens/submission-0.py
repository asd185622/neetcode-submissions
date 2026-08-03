class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        # visited = [[False for _ in range(n)] for _ in range(n)]
        # print(visited[:])

        def putQueen(visited,row,col):
            tmpVisited = [r[:] for r in visited]
            #row,col
            for i in range(n):
                tmpVisited[row][i] = True
                tmpVisited[i][col] = True
            #diagonal
            for i in range(1,n):
                if row + i <= n - 1 and col + i <= n - 1:
                    tmpVisited[row + i][col + i] = True
                if row + i <= n - 1 and col - i >= 0:
                    tmpVisited[row + i][col - i] = True
                if row - i >= 0 and col - i >= 0:
                    tmpVisited[row - i][col - i] = True
                if row - i >= 0 and col + i <= n - 1:
                    tmpVisited[row - i][col + i] = True
            return tmpVisited


            
        def backtracking(comb,visited,row):
            # print(comb,row)
            if row >= n:
                ans.append(comb[:])
                return
            
            tmp = ["."] * n
            # print(comb,visited,row)
            for i in range(n):
                if visited[row][i]:
                    # print(f"skip:{row},{i}")
                    continue
                # print(visited)
                tmp[i] = "Q"
                comb.append("".join(tmp))
                backtracking(comb,putQueen(visited,row,i),row + 1)
                tmp[i] = "."
                comb.pop()


        backtracking([],[[False for _ in range(n)] for _ in range(n)],0)
        return ans
                

