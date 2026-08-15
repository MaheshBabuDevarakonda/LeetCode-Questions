class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Current Time Complexity: O(log N) | Space Complexity: O(1)
        # Optimal Time Complexity: O(log N) | Space Complexity: O(1)
        
        n=len(nums)
        low=0
        high=n-1
        # BUG: 'min' is a built-in Python function. Using it as a variable name 
        # shadows the function, which causes the 'min(mini, nums[low])' call to fail.# FIXED: Changed 'min' to 'min_val' to avoid shadowing the built-in min() function.
        # HINT 1: Your logic 'if nums[low] <= nums[mid]' assumes the left side is always sorted.
        # While true, you are updating 'low = mid + 1' and taking 'nums[low]' as the min.
        # This will skip the actual minimum if it's located in the right half.
        
        # HINT 2: In a rotated sorted array, if nums[mid] > nums[high], 
        # the minimum MUST be to the right of mid (mid + 1).
        # If nums[mid] <= nums[high], the minimum is at mid or to the left.
        
        # HINT 3: Check your 'midvalue' initialization. If the loop doesn't execute 
        # or logic fails, it might throw an UnboundLocalError.
        mini=float("inf")
        while(low<=high):
            mid=(low+high)//2
            # COACHING: The condition 'nums[low] <= nums[mid]' tells you the left half is sorted.
            # The minimum in a sorted range is always at the start (nums[low]).
            # However, to truly find the pivot in a rotated array, comparing nums[mid] 
            # with nums[high] is more reliable for narrowing the search space.
            if nums[mid]<=nums[high]:
                mini=min(mini,nums[mid]) # This will throw TypeError because 'min' is an int (0)
                high=mid-1
            else:
                mini=min(mini,nums[low]) # This will throw TypeError because 'min' is an int (0)
                # BUG: You are moving 'high' in both branches. 
                # If nums[mid] > nums[high], the min is in the right half, so you should move 'low'.
                low=mid+1
        return mini
        
# COACH TIP: Your current logic doesn't correctly narrow down the pivot. 
# Try comparing nums[mid] with nums[high] instead of nums[low].
# If you get stuck, check the "Video Solutions" section in the Solutions tab on the left!
# 
# Analysis:
# Your current approach is O(log N), which is optimal, but the logic for updating 'low' and 'high' is incorrect.
# Currently, you decrease 'high' in both branches of the if/else, which prevents the search from moving right.
# 
# Step-by-step Fix:
# 1. If nums[mid] > nums[high], the pivot (min) is definitely to the right. Set low = mid + 1.
# 2. If nums[mid] <= nums[high], the pivot could be mid itself or to the left. Set high = mid.
# 3. Use a while low < high loop to avoid index errors and return nums[low] at the end.

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna