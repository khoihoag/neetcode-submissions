# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        len_head = 0
        while curr is not None:
            len_head += 1
            curr = curr.next
        
        curr = head
        
        if n == len_head:
            head = head.next
            return head
        
        elif n == 1:
            if head is None or head.next is None:
                return None
            secondLast = head
            while secondLast.next.next is not None:
                secondLast = secondLast.next
            secondLast.next = None
            return head

        else:
            curr = head
            pos = 1
            while pos < len_head-n:
                curr = curr.next            
                pos += 1
            curr.next = curr.next.next
            return head