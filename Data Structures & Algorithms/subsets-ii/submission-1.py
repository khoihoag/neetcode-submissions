class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        def backtrack(path, idx):
            ans.add(tuple(path.copy()))
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(path, i+1)
                path.pop()

        backtrack([], 0)
        return ([list(i) for i in list(ans)])