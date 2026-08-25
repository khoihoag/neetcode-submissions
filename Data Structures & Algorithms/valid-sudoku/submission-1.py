class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            res = set()
            for j in i:
                if j in res and j != '.':
                    return False
                res.add(j)

        for i in range(9):
            res = set()
            for j in range(9):
                n = board[j][i]
                if n in res and n != '.':
                    return False
                res.add(n)
        for row in [0, 3, 6]:
            for col in [0, 3, 6]:
                table = [
                    board[row][col], board[row][col + 1], board[row][col + 2],
                    board[row + 1][col], board[row + 1][col + 1], board[row + 1][col + 2],
                    board[row + 2][col], board[row + 2][col + 1], board[row + 2][col + 2],
                ]
                res = set()
                for i in table:
                    if i in res and i != '.':
                        return False
                    res.add(i)

        return True