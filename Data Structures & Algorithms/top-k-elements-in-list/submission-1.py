class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans =[]
        dic = defaultdict(int)

        for i in nums:
            dic[i] += 1
    
        sorted_dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=False))

        for i in list(sorted_dic.keys())[::-1]:
            if k > 0:
                ans.append(i)
                k -= 1

            if k == 0:
                return ans

