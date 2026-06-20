class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #check row
        for row in board:
            search = {}
            for digit in row:
                if digit != "." and digit not in search:
                    search[digit] = 1
                elif digit != ".":
                    print("row not ok")
                    return False
        
        #check column
        for column in range(9):
            search = {}
            for row in board:
                if row[column] not in search:
                    search[row[column]] = 1
                elif row[column] != ".":
                    print("col not ok")
                    return False
        
        #check sub-boxes
        for row in range(0,8,3):
            for col in range(0,8,3):
                search = {}
                for i in range(3):
                    for j in range(3):
                        if board[row + i][col + j] not in search:
                            search[board[row + i][col + j]] = 1
                        elif board[row + i][col + j] != ".":
                            print("sub-boxes not ok")
                            return False
        return True


                