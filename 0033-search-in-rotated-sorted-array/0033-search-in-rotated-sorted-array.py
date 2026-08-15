class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Time Complexity: O(log n) | Space Complexity: O(1)
        # Optimal Complexity: O(log n) | O(1)
        # Review: Your logic is almost correct, but there is a critical bug in the 'else' block.
        ans=-1
        n=len(nums)
        low=0
        high=n-1
        while(low<=high):
            mid=(low+high)//2
            if  nums[mid]==target:
                return mid
            elif nums[mid]<=nums[high]:
                if nums[mid]<=target<=nums[high]:
                    low=mid+1
                else:
                    # BUG: You are updating 'mid' instead of 'high'. 
                    # This creates an infinite loop or incorrect range.
                    # Change 'mid=mid-1' to 'high=mid-1'
                    high=mid-1
            else:
                if nums[low]<=target<=nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna