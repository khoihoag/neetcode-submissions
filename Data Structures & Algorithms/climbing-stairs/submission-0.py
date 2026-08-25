class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [1,1]
        if n <= 1:
            return steps[n]
        for i in range(2, n+1):
            steps.append(steps[i-1]+steps[i-2])

        return steps[-1]