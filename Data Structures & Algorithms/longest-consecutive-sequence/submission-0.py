class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        max_len = 0

        for i in nums:

            res = 0
            if i-1 not in hash_set:
                while i in hash_set:
                    print(i)
                    i += 1
                    res += 1
                print(res)
                if res > max_len:
                    max_len = res

        return max_len