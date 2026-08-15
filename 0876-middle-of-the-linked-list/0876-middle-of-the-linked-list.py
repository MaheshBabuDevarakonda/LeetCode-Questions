# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # COACHING NOTES:
        # 1. Bug: 'self.head' is incorrect. The head is passed as an argument 'head'. Use 'temp = head'.
        # 2. Bug: 'len(head)' does not work on Linked Lists. Linked Lists are not Python lists.
        # 3. Current Complexity: Time O(N), Space O(1). This is optimal, but the implementation has errors.
        # 4. HINT: You are using the 'Two-Pass' approach (find length, then find middle). 
        # 5. CHALLENGE: Can you solve this in a 'Single-Pass' using two pointers (Slow and Fast)?
        #    - Slow pointer moves 1 step, Fast pointer moves 2 steps. 
        #    - When Fast reaches the end, Slow will be at the middle.
        temp=head
        length=0
        while(temp!=None):
            temp=temp.next
            length+=1
        for i in range(0,length//2):
            head=head.next
        return head

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna