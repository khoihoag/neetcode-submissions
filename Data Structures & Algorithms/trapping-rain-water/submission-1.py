class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_area = 0
        pre_arr = [0] * n
        suf_arr = [0] * n
        max_pre = 0
        max_suf = 0

        for i in range(n):
            if max_pre < height[i]:
                max_pre = height[i]
            pre_arr[i] = max_pre

        for i in range(n-1, -1, -1):
            if max_suf < height[i]:
                max_suf = height[i]
            suf_arr[i] = max_suf

        for i in range(n):
            max_area += min(pre_arr[i], suf_arr[i]) - height[i]

        return max_area