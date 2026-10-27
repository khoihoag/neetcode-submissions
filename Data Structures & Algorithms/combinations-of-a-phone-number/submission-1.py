class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if digits == "":
            return []
        ans = ['']
        latters = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        for d in digits:
            ans = [x + ch for x in ans for ch in latters[int(d)]]
        return ans