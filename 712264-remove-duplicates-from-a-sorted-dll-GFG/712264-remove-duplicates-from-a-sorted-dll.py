# class Node:
#     def __init__(self, value):
#         self.data = value  # value stored in node
#         self.next = None
#         self.prev = None

class Solution:
    def removeDuplicates(self, headRef):
        myset=set()
        temp=headRef
        while(temp is not None):
            if temp.data in myset:
                temp.prev.next=temp.next
                
                if temp.next is not None:
                    temp.next.prev=temp.prev
                    
            else:
                myset.add(temp.data)
            temp=temp.next
        return headRef
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna