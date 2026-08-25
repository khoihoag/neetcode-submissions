class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def chan(i, j):
            res = 1
            for h in range(i, j+1):
                res *= h
            return res
        return chan(max(m, n), m+n-2)//chan(1, min(m,n)-1)