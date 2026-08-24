# Structure of Doubly Linked List Node
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def givenSumPairs(self, head, target):
        temp=head
        myset=set()
        res=[]
        while temp is not None:
            rem=target-temp.data
            if rem in myset:
                res.append([rem,temp.data])
            myset.add(temp.data)
            temp=temp.next
        res.sort()
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna