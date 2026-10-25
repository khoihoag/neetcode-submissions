class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_panlidrone(arr):
            return arr == arr[::-1]

        ans = []

        def backtrack(idx, path):
            if idx == len(s):
                ans.append(path.copy())
                return

            for i in range(idx, len(s)):
                part = s[idx:i + 1]

                if is_panlidrone(part):
                    path.append(part)
                    backtrack(i + 1, path)
                    path.pop()

        backtrack(0, [])
        return ans