class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        
        # dp[i] đại diện cho s[0:i]
        dp = [False] * (n + 1)
        dp[0] = True  # Chuỗi rỗng
        
        # Giới hạn độ dài từ để không duyệt thừa
        max_len = max(len(w) for w in words) if words else 0

        for i in range(1, n + 1):
            # Chỉ cần lùi j tối đa bằng độ dài từ dài nhất trong từ điển
            for j in range(i - 1, max(-1, i - max_len - 1), -1):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break  # Đã tìm thấy một cách cắt hợp lệ cho s[0:i], dừng sớm

        return dp[n]