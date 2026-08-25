class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has = set()
        for i in range(0, len(nums)):
            if nums[i] in has:
                return True
            else:
                has.add(nums[i])
        return False