class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = 1

        for i in range(1, len(nums)):
            max_len = 0
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    max_len = max(max_len, dp[j])

            if max_len != 0: dp[i] = max_len + 1
            else: dp[i] = 1
        return max(dp)
