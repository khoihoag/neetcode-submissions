
class Solution:
    def subsets (self, nums):
        path = []
        result = []
        def backtrack (start, path):
            result.append(path.copy())
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
            return result
        return backtrack(0, [])