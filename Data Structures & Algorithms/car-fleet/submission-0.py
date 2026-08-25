class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p, s] for p, s in zip(position, speed)]        # zip -> lấy từng phần tử cảu 2 list tạo thành 1 tuple 
        stack = []

        for p, s in sorted(cars)[::-1]:     # vì không biết xe nào đang đứng trước xe nào -> sort
                                            # vì xe phía sau không thể vượt qua xe trước, nên nếu xe đứng thấp hơn mà đi nhanh hơn sẽ cùng với xe đứng trước đi chậm hơn lập thành 1 đội
            time_taken = (target - p)/s    
            if not stack or stack[-1] < time_taken:
                stack.append(time_taken)
        return len(stack)
