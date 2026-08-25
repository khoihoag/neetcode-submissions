class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for nums in matrix:
            n = len(nums)
            l, r = 0, n - 1
            while l <= r:
                m = l + (r-l)//2
                if nums[m] == target:
                    return True
                elif nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
        return False