class Solution:
    def encode(self, strs: List[str]) -> str:
        s = ""

        for sub_str in strs:

            for i in sub_str:
                s += str(ord(i)) + '#'

            s += '!'
        return s

    def decode(self, s: str) -> List[str]:
        strs =[]
        res = ''
        i = 0
        n = len(s)

        while i < n:
            num = ""

            while '0' <= s[i] <= '9' and i < len(s):
                num += s[i]
                i += 1

            if num != "":
                res += chr(int(num))

            if s[i] == '!':
                strs.append(res)
                res = ''

            i += 1
        return strs  