class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ans = False

        def backtracking(comb,wordSet,row,col,index):
            # print(row,col,comb)
            nonlocal ans
            # if "".join(comb) == word:
            #     ans = True
            #     return
            if board[row][col] != word[index] or (row,col) in wordSet or ans:
                return

            comb.append(board[row][col])
            wordSet.add((row,col))
            if "".join(comb) == word:
                ans = True
                return

            # print(row,col,comb)
            if row > 0:
                # print("go up")
                backtracking(comb,wordSet,row - 1,col,index + 1)
            if col < len(board[0]) - 1:
                # print("go right")
                backtracking(comb,wordSet,row,col + 1,index + 1)
            if row < len(board) - 1:
                # print("go down")
                backtracking(comb,wordSet,row + 1,col,index + 1)
            if col > 0:
                # print("go left")
                backtracking(comb,wordSet,row,col - 1,index + 1)
            comb.pop()
            wordSet.discard((row,col))
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    wordSet = set()
                    print("for loop find first char:",row,col,board[row][col])
                    backtracking([],wordSet,row,col,0)
                if ans:
                    return True
        
        return ans