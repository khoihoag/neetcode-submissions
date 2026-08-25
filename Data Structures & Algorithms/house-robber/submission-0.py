class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        elif len(nums) == 3:
            return max(nums[0]+nums[2], nums[1])

        else:
            dp = [i for i in nums]
            dp[2] = dp[0] + nums[2]
            for i in range(3, len(nums)):
                dp[i] = max(dp[i-2], dp[i-3])+nums[i]
            return max(dp)