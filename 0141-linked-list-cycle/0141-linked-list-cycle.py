# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Coaching Analysis:
        # Your logic is attempting Floyd's Cycle-Finding Algorithm (Tortoise and Hare),
        # but there is a critical bug in how you update your pointers.
        
        # 1. Problem: You are using 'temp' to update 'fast' and 'slow', but 'temp' 
        #    never changes inside the loop. This means 'fast' and 'slow' 
        #    will just keep jumping to the same two nodes repeatedly.
        # 2. Fix: Update 'fast' and 'slow' based on their own current positions.
        
        # Current Complexity:
        # Time: O(N) - but currently results in an infinite loop or wrong answer.
        # Space: O(1)
        # Optimal Complexity: Time O(N), Space O(1).
        
        temp=head
        fast=head
        slow=head
        while(fast is not None and fast.next is not None):
            # HINT: Instead of 'temp.next', use 'fast.next.next' and 'slow.next'
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                return True
        return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna