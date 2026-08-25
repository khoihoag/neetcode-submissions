# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        while list1 is not None and list2 is not None:
            if list1.val > list2.val:
                curr.next = ListNode(list2.val)
                list2 = list2.next

            elif list1.val < list2.val:
                curr.next = ListNode(list1.val)
                list1 = list1.next
            
            else:
                curr.next = ListNode(list1.val)
                curr = curr.next
                curr.next = ListNode(list2.val)
                list1 = list1.next
                list2 = list2.next

            curr = curr.next

        if list1 is None:
            curr.next = list2

        elif list2 is None:
            curr.next = list1    

        dummy = dummy.next

        return dummy