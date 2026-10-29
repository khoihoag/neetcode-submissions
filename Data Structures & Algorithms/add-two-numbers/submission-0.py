# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number1 = 0
        number2 = 0
        res = 1

        curr = l1
        while curr:
            number1 += (curr.val * res)
            res *= 10 
            curr = curr.next

        res = 1
        curr = l2
        while curr:
            number2 += (curr.val * res)
            res *= 10
            curr = curr.next
        
        total = list(map(int, str(number1+number2)))
        ans = ListNode(total[-1])
        curr = ans
        for i in range(len(total)-2, -1, -1):
            curr.next = ListNode(total[i])
            curr = curr.next
        
        return ans