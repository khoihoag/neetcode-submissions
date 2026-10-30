class Solution:
    def countSubstrings(self, s: str) -> int:
        n =  len(s)
        dp = [[False] * n for _ in range(n)]

        count = n

        for i in range(n):
            dp[i][i] = True
        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i + length - 1

                if s[i] == s[j] and (dp[i+1][j-1] or j == i+1):
                    dp[i][j] = True
                    count += 1
        return count 
