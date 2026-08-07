class Solution:
    def findFloor(self, arr, x):
        # code here
        # COACH REVIEW:
        # Your current logic is implementing a 'Lower Bound' search (finding the first element >= x).
        # For 'Floor', you need the largest element <= x.
        # 1. Issue: if arr[mid] >= x, you are updating lb. For floor, you should update when arr[mid] <= x.
        # 2. Issue: if arr[mid] > x, you must move the high pointer (h = mid - 1).
        # 3. Issue: l = l + 1 should be l = mid + 1 for binary search efficiency.
        # Current Time Complexity: O(log N) - Correct approach, but wrong condition.
        # Current Space Complexity: O(1) - Optimal.
        # Hint: Change the condition to check if arr[mid] <= x, update your answer, and move the left pointer.
        n=len(arr)
        ans=-1
        low=0
        high=n-1
        while low <= high:
            mid = (low + high) // 2
            
            # If arr[mid] is less than x, it could be the floor
            if arr[mid]<=x:
                ans = mid
                low = mid + 1
            
            # If arr[mid] is greater than x, the floor must be on the left
            else:
                high = mid - 1
                
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna