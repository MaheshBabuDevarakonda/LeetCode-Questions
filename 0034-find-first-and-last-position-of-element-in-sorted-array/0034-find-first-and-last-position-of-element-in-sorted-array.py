class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Current Time Complexity: O(log N) - Binary Search approach
        # Current Space Complexity: O(1)
        # Optimal Complexity: O(log N) Time, O(1) Space
        
        lb=-1
        ub=-1
        low=0
        high=len(nums)-1

        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                lb=mid
                high=mid-1
            elif nums[mid]>target:
                high=mid-1
            else: 
                low=mid+1
        if lb==-1:return [-1,-1]
        high=len(nums)-1
        # BUG ALERT: The 'low' and 'high' variables were modified by the first while loop.
        # You must reset 'low = 0' and 'high = len(nums) - 1' before starting the second binary search.
        # Otherwise, the second loop will not execute or will search the wrong range.
        # COACH: You have correctly identified the need to reset pointers. I have uncommented the reset logic below.
        
        # Reset pointers here:
        low = 0
        high = len(nums) - 1

        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                ub=mid
                low=mid+1
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
            
        
        # LOGIC CHECK: Your 'ub' logic currently finds the first element GREATER than target.
        # To find the last occurrence of target, you should store 'mid' when nums[mid] == target 
        # and move 'low = mid + 1'.
        # COACH: To fix this, change the condition to: if nums[mid] <= target: ub = mid; low = mid + 1
        # This ensures 'ub' tracks the rightmost occurrence of the target.
        
        # Final Validation: After finding lb and ub, check if nums[lb] == target (handling index -1) 
        # to ensure the target actually exists in the array.
        return [lb,ub]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna