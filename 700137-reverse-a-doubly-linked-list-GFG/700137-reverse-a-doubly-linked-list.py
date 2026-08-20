""" Structure of Doubly Linked List Node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        if head.next is None:
            return head
        # code here
        curr=head
        prev=None
        while(curr is not None):
            front=curr.next
            curr.next=prev
            curr.prev=front
            prev=curr
            curr=front
        return prev
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna