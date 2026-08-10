class Solution:
    def countFreq(self, arr, target):
        first=-1
        last=0
        # code here
        # COACH ANALYSIS:
        # Your current logic has a critical bug: the 'if first == -1: return 0' block 
        # is inside the loop. This causes the function to return 0 immediately if 
        # the first element of the array is not the target.
        #
        # Time Complexity: O(n) - Linear scan.
        # Space Complexity: O(1) - Constant space.
        #
        # HINT: Move the 'if first == -1' check OUTSIDE the for loop. 
        # Also, consider if there is a more optimal way to find boundaries 
        # in a sorted array (e.g., Binary Search O(log n)).
        for i in range(len(arr)):
            if arr[i]==target:
                if first==-1:
                    first=i
                last=i
        if first==-1:
            return 0
        return last-first+1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna