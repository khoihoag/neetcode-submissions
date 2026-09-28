class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stack = sorted(stones)

        while len(stack) > 1:
            s1 = stack.pop()
            s2 = stack.pop()

            if s1 != s2:
                res = s1-s2
                stack.append(res)
                for i in range(len(stack)-2, -1, -1):
                    if stack[i+1] < stack[i]:
                        stack[i+1], stack[i] = stack[i], stack[i+1]

        return stack[-1] if len(stack)== 1 else 0