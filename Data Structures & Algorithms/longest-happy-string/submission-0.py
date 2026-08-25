import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Bước 1: Khởi tạo Max-Heap
        # Lưu trữ dưới dạng tuple (-số_lượng, 'ký_tự')
        max_heap = []
        if a > 0: heapq.heappush(max_heap, (-a, 'a'))
        if b > 0: heapq.heappush(max_heap, (-b, 'b'))
        if c > 0: heapq.heappush(max_heap, (-c, 'c'))
        
        res = [] # Mảng chứa các ký tự của chuỗi kết quả
        
        while max_heap:
            # Lấy ra ký tự đang có số lượng nhiều nhất
            count1, char1 = heapq.heappop(max_heap)
            
            # Bước 2 & 3: Kiểm tra an toàn (xem 2 ký tự cuối đã giống char1 chưa)
            if len(res) >= 2 and res[-1] == res[-2] == char1:
                # TRƯỜNG HỢP BỊ KẸT: Bắt buộc phải dùng ký tự nhiều thứ 2
                
                # Bước 4 (Điểm mù): Nếu không còn ký tự nào khác -> Dừng sớm
                if not max_heap:
                    break 
                
                # Lấy ký tự nhiều thứ 2 ra
                count2, char2 = heapq.heappop(max_heap)
                res.append(char2)
                count2 += 1 # Giảm số lượng đi 1 (vì đang là số âm nên dùng phép +1)
                
                # Nếu vẫn còn dư, đẩy lại vào heap
                if count2 < 0:
                    heapq.heappush(max_heap, (count2, char2))
                
                # Quan trọng: Đẩy lại ký tự nhiều nhất (char1) vào heap để dùng cho vòng lặp sau
                heapq.heappush(max_heap, (count1, char1))
                
            else:
                # TRƯỜNG HỢP AN TOÀN: Thoải mái ghép ký tự nhiều nhất vào
                res.append(char1)
                count1 += 1 # Giảm số lượng đi 1
                
                # Nếu vẫn còn dư, đẩy lại vào heap
                if count1 < 0:
                    heapq.heappush(max_heap, (count1, char1))
                    
        # Nối các ký tự trong mảng thành chuỗi hoàn chỉnh
        return "".join(res)