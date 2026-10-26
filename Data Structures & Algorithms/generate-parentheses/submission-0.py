class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        p = ['(', ')']

        def backtrack(s, l, r):
            # l là số lượng ngoặc mở, r là số lượng ngoặc đóng
            print(s)
            if len(s) == n*2:
                ans.append("".join(s))
                return 

            for i in p:
                if i == '(' and l < n:
                    print(l, n)
                    s.append(i)
                    backtrack(s, l+1, r)
                    s.pop()

                elif i == ')' and r < l:
                    s.append(i)
                    backtrack(s, l, r+1)
                    s.pop()
                
        backtrack([], 0, 0)
        return ans