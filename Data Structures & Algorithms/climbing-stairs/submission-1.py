class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)

        def climb(n, i):
            if i == 1 or i ==0:
                return 1
            if dp[i] != 0:
                return dp[i]
            dp[i] = climb(n, i-1) + climb(n, i-2)
            return dp[i]
        return climb(n, n)