# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mid, end = head, head

        while end and end.next:
            mid = mid.next
            end = end.next.next

        list2 = mid.next
        mid.next = None

        # head - mid, list2 - 

        prev, curr = None, list2
        if list2:
            next = list2.next
        while curr:
            curr.next = prev
            prev = curr
            curr = next
            if curr:  
                next = curr.next
        
        curr1, curr2 = head, prev
        while curr1 and curr2:
            temp = curr2.next
            curr2.next = curr1.next
            curr1.next = curr2
            curr2 = temp
            curr1 = curr1.next.next



