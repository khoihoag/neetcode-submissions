class Solution:
    def permute(self, nums):
        result = []

        used = len(nums) * [False]
        def backtrack(path):
            if len(path) == len(nums):
    
                result.append(path.copy())
                return

            for i in range(len(nums)):
                if used[i] == False:
                    path.append(nums[i])
                    used[i] = True
                    backtrack(path)
                    path.pop()
                    used[i] = False
        backtrack([])

            
        return result

