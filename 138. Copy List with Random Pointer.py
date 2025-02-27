#space: O(1)
#time: O(n)
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
        # step 1 make copy of each node and point its next to the copied node
        if head is None:
            return
        curr= head
        while curr is not None:
            copy= Node(curr.val)
            copy.next = curr.next
            curr.next= copy
            curr= copy.next

        # step 2 update the random pointers for the copied nodes
        copyhead= head.next
        curr = head
        while curr is not None:
            copy = curr.next
            if curr.random is not None and copy.random is None :
                copy.random = curr.random.next
            curr= curr.next.next
        #step 3 updating the next pointers
        curr= head
        while curr.next.next is not None:
            copynode= curr.next
            curr.next= copynode.next
            copynode.next= curr.next.next
            curr= curr.next
        return copyhead
        
