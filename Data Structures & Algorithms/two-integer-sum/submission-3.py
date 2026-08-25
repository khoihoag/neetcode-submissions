class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has = {}
        for i, n in enumerate(nums):
            res = target - nums[i]
            if res in has:
                return [has[res], i]

            has[n] = i