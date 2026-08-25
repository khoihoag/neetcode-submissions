# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def ModifyArr(head):
            curr = head
            arr = []

            while curr is not None:
                arr.append(curr.val)
                curr = curr.next
            
            return arr

        arr = ModifyArr(head)
        left, right = 1, len(arr)-1
        curr = head
        curr = curr.next

        while left < right:
            curr.val = arr[right]
            right -= 1
            curr.next.val = arr[left]
            left += 1
            curr = curr.next.next

            if left == right:
                curr.val = arr[right]
                return 
        return
