class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {

        }
        ans = []
        for i in nums:
            if i not in count.keys():
                count[i] = 0
            count[i] += 1
        print(count, len(count)/3)
        for i in count.items():
            if i[1] > len(nums)/3:
                ans.append(i[0])
        return ans