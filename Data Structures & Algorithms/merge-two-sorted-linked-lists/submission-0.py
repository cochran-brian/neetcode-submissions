# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1

        head = None
        curr = head
        curr1 = list1
        curr2 = list2
        while curr1 != None and curr2 != None:
            if curr1.val <= curr2.val:
                if curr == None:
                    head = ListNode(val=curr1.val)
                    curr = head 
                else:
                    curr.next = ListNode(val=curr1.val)
                    curr = curr.next
                curr1 = curr1.next
            else:
                if curr == None:
                    head = ListNode(val=curr2.val)
                    curr = head
                else:
                    curr.next = ListNode(val=curr2.val)
                    curr = curr.next
                curr2 = curr2.next

        if curr1 == None and curr2 != None:
            curr.next = curr2
        elif curr2 == None and curr1 != None:
            curr.next = curr1

        return head