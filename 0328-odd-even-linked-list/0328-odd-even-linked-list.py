# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # COACH: Your current logic has a critical bug in the base case and the loop.
        # 1. Base Case: 'if head is None and head.next is None' will crash if head is None.
        #    Use 'if not head or not head.next: return head'.
        if not head or  head.next is None:
            return head
        even=head.next
        odd=head
        evenhead=even
        while(even is not None and even.next is not None):
            # COACH: You are updating 'even' before 'odd' uses its original value.
            # This causes 'odd.next.next' to skip nodes incorrectly.
            # HINT: Update odd.next first, then move odd, then update even.next, then move even.
            odd.next=even.next
            odd=odd.next
            even.next=odd.next
            even=even.next
        odd.next=evenhead
        return head
        # TIME COMPLEXITY: O(N) - Linear scan of the list.
        # SPACE COMPLEXITY: O(1) - In-place rearrangement.
        # This is the optimal complexity. Now that the pointer logic is corrected, you can submit!
        # If you get stuck, check the "Video Solutions" tab in the LeetHub editor!

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna