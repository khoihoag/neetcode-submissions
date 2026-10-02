#  Combination Sum: từ một mangr gồm các số nguyên cho trước, tìm ra tất cả sự kết hợp giữa các số có tổng = target, một số có thể sử dụng nhiều lần

class Solution: 
    def combinationSum (self, nums, target):
        result = []
        pitch = []

        nums.sort()

        def backtrack(start, target, pitch):
            if target == 0:
                result.append(pitch.copy())
                return

            for i in range(start, len(nums)):
                num = nums[i]

                if target - num < 0:
                    return
                pitch.append(num)
                backtrack(i, target-num, pitch)
                pitch.pop()
        backtrack(0, target, pitch)
        return result