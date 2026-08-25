class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        n = len(heights)
        l, r = 0, n-1
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            print(area, heights[l], heights[r])
            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                if heights[l+1] > heights[r-1] and l + 1 < r - 1:
                    l += 1
                elif heights[l+1] < heights[r-1] and l + 1 < r - 1:
                    r -= 1
                else:
                    r -= 1
            max_water = max(area, max_water)

        return max_water