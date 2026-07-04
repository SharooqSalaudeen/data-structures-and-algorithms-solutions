from collections import defaultdict 
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(list)
        col = defaultdict(list)
        square = defaultdict(list)

        for r in range(9):
            for c in range(9):
                if (board[r][c] in row[r]
                    or board[r][c] in col[c]
                    or board[r][c] in square[r//3,c//3]):
                        return False
                
                if board[r][c] == ".":
                    continue
                
                row[r].append(board[r][c])
                col[c].append(board[r][c])
                square[r//3, c//3].append(board[r][c])

        return True