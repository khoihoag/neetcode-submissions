class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        path = []

        def backtrack(idx, path, sum_path):
            if sum_path == target:
                
                ans.append(path.copy())
                    
                return

            for i in range(idx, len(candidates)):
                if (sum_path + candidates[i]) > target:
                    break
                if i > idx and candidates[i] == candidates[i-1]:
                    continue 
                path.append(candidates[i])
                sum_path += candidates[i]
                backtrack(i+1, path, sum_path)
                sum_path -= path.pop()

        backtrack(0, path, 0)
        return ans
