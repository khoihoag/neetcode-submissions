class Solution:
    def search(self, nums: List[int], target: int) -> int:
       # tìm target rng đoạn con
        def binary_search(left, right, nums, target):
            while left <= right:
                mid = (left + right)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return -1

        # Tìm vị trí phần tử nhỏ nhất
        n = len(nums)
        l, r = 0, n - 1
        pivot = 0
        while l <= r:
            if nums[l] < nums[r]:
                if nums[pivot] > nums[l]:
                    pivot = l
                break

            m = (l+r)//2
            if nums[m] < nums[pivot]:
                pivot = m

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        # Tìm vị trí target
        if target > nums[n-1]:
            return binary_search(0, pivot-1, nums , target)
        else:
            return binary_search(pivot, n-1, nums, target)
            