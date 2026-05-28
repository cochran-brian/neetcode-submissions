"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hmap = {}
        curr = head
        while curr:
            hmap[curr] = Node(x=curr.val, next=None, random=None)
            curr = curr.next

        curr = head
        dummy = Node(x=0)
        new_curr = dummy
        while curr:
            new_curr.next = hmap[curr]
            if curr.random == None:
                new_curr.next.random = None
            else:
                new_curr.next.random = hmap[curr.random]
            new_curr = new_curr.next
            curr = curr.next
        
        return dummy.next