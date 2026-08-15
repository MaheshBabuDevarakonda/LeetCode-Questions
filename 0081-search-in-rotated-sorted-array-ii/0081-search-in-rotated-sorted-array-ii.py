class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Coach: Your logic for handling duplicates (nums[low]==nums[mid]==nums[high]) is correct!
        # However, there is a bug in your pointer initialization.
        n=len(nums)
        low=0
        high=n-1 # BUG: You initialized n as len(nums)-1, then high as n-1. 
                 # This means high = len(nums)-2, skipping the last element of the array.
        # Fix: Either use n=len(nums) and high=n-1, or just high=len(nums)-1.
        
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                return True
            elif nums[low]==nums[mid]==nums[high]:
                low=low+1
                high=high-1
                continue
            elif nums[mid]<=nums[high]:
                if nums[mid]<=target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
            else:
                if nums[low]<=target<=nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
        return False

# Complexity Analysis:
# Time Complexity: Average O(log N), Worst Case O(N) when all elements are the same.
# Space Complexity: O(1).
# This is the optimal approach for this problem. Once you fix the 'high' pointer initialization, you are ready to submit!

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna