class Solution:
    def isPalindrome(self, s: str) -> bool:
        trans_s = ""

        for i in s:
            i = i.lower()

            if 'a' <= i <= 'z' or '0' <= i <= '9':
                trans_s += i

        n = len(trans_s)
        l, r = 0, n-1

        while l < r:

            if trans_s[l] != trans_s[r]:
                return False

            l += 1
            r -= 1

        return True
