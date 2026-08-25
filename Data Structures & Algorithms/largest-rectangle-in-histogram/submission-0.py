class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n = len(heights)
        s_pre = [0] * n
        s_suf = [0] * n
        stack = [0] * n
        max_area = 0

        for i in range(len(heights)):

            while stack != [] and heights[i] < heights[stack[-1]]:
                s_pre[stack[-1]] = heights[stack[-1]] * (i - stack[-1])

                stack.pop()

                if stack != []:
                    s_suf[i] = heights[i] * (i - stack[-1] - 1 )
                else:
                    s_suf[i] = heights[i] * i
            stack.append(i)
    
        while stack != []:
            s_pre[stack[-1]] = heights[stack[-1]] * (n - stack[-1])
            stack.pop()

        for i in range(n):
            max_area = max(s_pre[i]+s_suf[i], max_area)

        return max_area
    