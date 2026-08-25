class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == ['""']:
            return [[""]]
        dic = {}
        ans = []
        for i in strs:
            sorted_i = "".join(sorted(i))

            if sorted_i in dic.keys():
                dic[sorted_i].append(i)
            else:
                dic[sorted_i] = [i]

        for i in dic.keys():
            ans.append(dic[i])

        return ans