class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = []
        nums.sort()
        n = len(nums)

        m = 1

        while m < n -1:
            l, r = 0, n-1
            
            while l < m < r and l >= 0 and r < n:
                sum = nums[l] + nums[m] + nums[r]

                if sum == 0:
                    arr.append([nums[l], nums[m], nums[r]])
                    l += 1
                    r -= 1

                elif sum < 0:
                    l += 1

                else:
                    r -= 1

            m += 1
        dic={}

        for i in arr:
            if i[0] not in dic.keys():
                dic[i[0]] = [i]
            else:
                if i not in dic[i[0]]:
                    dic[i[0]].append(i)
        print(dic)
        arr= []
        for i in dic.keys():
            for j in dic[i]:
                arr.append(j)

        return arr