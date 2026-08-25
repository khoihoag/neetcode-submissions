class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        dic = {}
        i = 0
        
        for j in range(len(s)):
            #tạo 1 mảng tần số
            if s[j] not in dic.keys():
                dic[s[j]] = 0
            dic[s[j]] += 1
            
            max_char = max(dic.values())
            # Số kí tự cần thay thế = độ dài dãy - tần số lớn nhất trong dãy
            # Nếu số kí tự cần thay thế > k thu gọn dãy = cách cho i tiến lên
            while (j-i+1) - k > max_char:
                dic[s[i]] -= 1
                i += 1
                
            res = max(res, j-i+1)

        return res
