class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []

        for i in range(n):

            if stack == []:
                stack.append(i)
            else:
                while stack != [] and temperatures[stack[-1]] < temperatures[i]:
                    answer[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
        return answer