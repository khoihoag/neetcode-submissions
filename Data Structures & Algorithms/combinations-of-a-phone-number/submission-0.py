class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
            }

        ans = []
        def backtrack(path, i_digit):
            if len(path) == len(digits):
                ans.append(''.join(path.copy()))
                return
            digit = digits[i_digit]
            for i in dict[digit]:
                path.append(i)
                backtrack(path, i_digit+1)
                path.pop()
        
           
           
           
        backtrack([], 0)
        return ans