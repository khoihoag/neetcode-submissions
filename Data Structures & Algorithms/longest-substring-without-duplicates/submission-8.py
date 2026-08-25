class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0

        l, r =0, 1
        n = len(s)
        max_len = 1
        sub_len=1

        while r < n:
            hash_set = set(s[l:r])

            if s[r] in hash_set:
                while s[l] != s[r]:
                    l += 1
                l += 1
                sub_len = r - l + 1
            else:
                sub_len += 1
                max_len = max(max_len, sub_len)
            r += 1

        return max_len

