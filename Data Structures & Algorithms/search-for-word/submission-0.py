class Solution:
    def exist(self, board, word):
        res = []
        cols = len(board[0])
        
        # Top padding row
        res.append([""] * (cols + 2))
        
        # Board rows with left and right padding
        for row in board:
            temp = [""] + list(row) + [""]
            res.append(temp)
            
        # Bottom padding row
        res.append([""] * (cols + 2))

        w = list(word)
        step = set()

        def backtrack(k, i, j):
            if k == len(w):
                return True

            if res[i][j] != w[k] or (i, j) in step:
                return False
            
            step.add((i, j))
            
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for di, dj in directions:
                next_i, next_j = i + di, j + dj
                if backtrack(k + 1, next_i, next_j):
                    return True
            step.remove((i, j))
            return False
        for i in range(1, len(res) - 1):
            for j in range(1, len(res[0]) - 1):
                if res[i][j] == w[0]:
                    if backtrack(0, i, j):
                        return True
                        
        return False

