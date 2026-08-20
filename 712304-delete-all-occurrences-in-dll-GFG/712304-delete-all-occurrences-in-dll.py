"""
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

"""
class Solution:
    def deleteAllOccurOfX(self, head, x):
        ans=[]
        # code here
        temp=head
        if temp.next is None :
            if temp.data==x:
                return None
            else :
                return head
            
        while(temp is not None):
            if temp.data!=x:
                ans.append(temp.data)
            temp=temp.next
        temp=head
        if len(ans) == 0:
            return None
        for i in range(len(ans)):
            e=ans[i]
            temp.data=e
            temp=temp.next
        if temp is not None:
            temp.prev.next = None
            temp.prev = None

        return head
        
            
                
                
        
            
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna