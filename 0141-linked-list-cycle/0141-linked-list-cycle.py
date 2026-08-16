# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Current Complexity:
        # Time: O(n^2) because 'if temp in arr' performs a linear search on the list every iteration.
        # Space: O(n) to store nodes in the array.
        # Optimal Complexity: Time O(n), Space O(1).
        
        arr=set()
        temp=head
        
        while(temp is not None):
            if temp in arr:
                return True
            arr.add(temp)
            temp=temp.next
        return False
        
        # COACHING HINTS:
        # 1. Logic Fix: Move the 'if temp in arr' check BEFORE the 'arr.append(temp)' line.
        # 2. Efficiency: Using a Python 'set()' instead of a 'list' for 'arr' would reduce the 
        #    lookup time from O(n) to O(1), making the overall time complexity O(n).
        # 3. Challenge: Can you solve this without using any extra space (O(1) space)? 
        #    Research "Floyd's Cycle-Finding Algorithm" (Two Pointers: Slow and Fast).
        # 4. If you get stuck on the O(1) approach, check the "Video Solutions" tab in the LeetHub editor!

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna