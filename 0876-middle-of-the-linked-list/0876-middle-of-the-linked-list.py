# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # COACH ANALYSIS:
        # Your current logic has a few critical issues:
        # 1. The loop condition `while(temp is not None)` will run until temp is null, 
        #    meaning you'll return None instead of the middle node.
        # 2. `temp=temp.next` followed by `temp=temp.next.next` moves the pointer 3 steps total per iteration.
        # 3. This will likely cause an 'AttributeError: NoneType has no attribute next' when reaching the end.
        #
        # HINT: Try the "Two-Pointer Approach" (Tortoise and Hare).
        # - Use a 'slow' pointer that moves 1 step at a time.
        # - Use a 'fast' pointer that moves 2 steps at a time.
        # - When the 'fast' pointer reaches the end, the 'slow' pointer will be exactly at the middle.
        #
        # Complexity of your current attempt:
        # Time: O(N), Space: O(1) - but it crashes/returns wrong result.
        # Optimal: Time O(N), Space O(1).
        slow=head
        fast=head
        # FIX: You don't need a 'temp' variable. Use the 'fast' pointer to control the loop.
        # The loop should run as long as fast and fast.next are not None.
        while(fast is not None and fast.next is not None):
            slow=slow.next
            fast=fast.next.next
        return slow

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna