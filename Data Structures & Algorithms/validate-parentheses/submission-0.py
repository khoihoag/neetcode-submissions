class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {']':'[', '}':'{', ')':'('}
        for i in s:
            n = len(stack) - 1
            if i in set(mapping.values()):
                stack.append(i)
            else:
                if stack == []:
                    return False
                elif stack[n] != mapping[i]:
                    return False 
                else:
                    stack.pop()

        return not stack